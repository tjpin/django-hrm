from datetime import timedelta, datetime

from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.views.decorators.http import require_http_methods 
from django.db.models import Q

from src.account.models import AccountUser
from src.office.applications import (LeaveApplication, LeaveStatus, timezone)
from src.office.hrd import (Training, Announcement)
from src.office.forms import (TrainingForm, AnnouncementForm, AppointmentForm)
from src.staff.models import (StaffNextBirthday, Staff, Department)
from .forms import (SettingsForm, SystemSettings)
from src.recruitment.models import (Vacancy, Application, Recruit)
from src.office.models import (Appointment, AppointmentStatus)


@login_required(login_url='login')
# @cache_page(60*15)
def dashboard(request):
    two_days_ago = timezone.now() - timedelta(days=2)

    recruits = Recruit.objects.all()[:3]
    vacancies = Vacancy.objects.all()
    leaves = LeaveApplication.objects.select_related('staff').filter(
            Q(status=LeaveStatus.APPROVED) & 
            Q(start_date__lt=timezone.now().date())
        ) .order_by('start_date')[:3]
    applications = Application.objects.all()
    appointments = Appointment.objects.filter(status=AppointmentStatus.PENDING).order_by('-date')
    birthdays = StaffNextBirthday.upcoming_birthdays().order_by('dob')[:3]
    admins = AccountUser.objects.filter(Q(is_superuser=True) & Q(is_staff=True)).order_by('-last_login')[:5]
    trainings = Training.objects.filter(Q(completed=False)).order_by('-date')[:3]
    announcements = Announcement.objects.select_related('sender').filter(date_announced__gte=two_days_ago).order_by("-date_announced")[:3]
    context = {
        "admins": admins,
        "leaves": leaves,
        "recruits": recruits,
        "vacancies": vacancies,
        "trainings": trainings,
        "birthdays": birthdays,
        'appointments': appointments,
        "applications": applications,
        "announcements": announcements,
    }
    return render(request, 'pages/dashboard.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        user_found = AccountUser.objects.filter(email=email).exists()
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            if user_found:
                messages.add_message(request, messages.INFO , "check email or password")
            else:
                messages.add_message(request, messages.INFO , "user does not exist")
            return render(request, 'pages/login-page.html')
                
    return render(request, 'pages/login-page.html')

def staffs_per_deparment(request, id):
    department = Department.objects.get(id=id)
    department_staffs = Staff.objects.filter(department=department).order_by('first_name')
    context = {'department_staffs': department_staffs, 'department': department}
    return render(request, "partials/department-staffs.html", context)

@csrf_exempt
@require_http_methods(['POST'])
def update_settings(request):
    sys_settings = SystemSettings.objects.first()
    print()
    print(request)

    logo = request.FILES.get('id_company_logo', None)
    if not logo:
        logo = sys_settings.company_logo
    useName = request.POST.get('use_name')

    SystemSettings.objects.update_or_create(
        company_name=request.POST.get('company_name'),
        company_logo=logo,
        use_name=True if useName == 'on' else False,
        company_address=request.POST.get('company_address'),
        company_email=request.POST.get('company_email'),
        company_mobile_number=request.POST.get('company_mobile_number'),
        company_zip=request.POST.get('company_zip'),
        currency=request.POST.get('currency')
    )
    return redirect('/')

def add_training(request):
    form = TrainingForm()
    if request.method == "POST":
        form = TrainingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, 'partials/training_form.html', {'form': form})

def add_announcement(request):
    form = AnnouncementForm()
    if request.method == "POST":
        form = AnnouncementForm(request.POST or None, request.FILES.get('file', None))
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, 'partials/announcement.html', {'form': form})

def add_appointment(request):
    form = AppointmentForm()
    if request.method == "POST":
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, 'partials/appointment.html', {'form': form})

def refresh(request):
    cache.clear()
    return redirect('/')