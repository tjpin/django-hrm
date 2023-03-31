from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, ListView, FormView
from django.contrib import messages

from .models import Application, Recruit, Recruitment, Vacancy
from .forms import RecruitForm, ApplicationForm
from src.staff.models import Staff, StaffStatusChoices

class RecruitmentHomeView(ListView):
    queryset = Recruitment.objects.select_related('vacancy').order_by('-date')
    template_name = 'pages/recruitment.html'
    context_object_name = 'recruitments'

    def get_context_data(self, **kwargs):
        context = super(RecruitmentHomeView, self).get_context_data(**kwargs)
        context['applications'] = Application.objects.all().order_by('-date')
        context['recruits'] = Recruit.objects.all()
        return context

@require_http_methods(["GET", "POST"])
def add_recruit(request):
    form = RecruitForm()
    if request.method == 'POST':
        form = RecruitForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('recruitment')
        print()
        print(form.errors)
        return redirect('recruitment')
    return render(request, 'partials/add-recruit.html', {'form': form})

def promote_recruit(request, pk):
    recruit = Recruit.objects.get(pk=pk)
    db_staff = None
    try:
        db_staff = Staff.objects.get(email=recruit.email)
    except:
        if db_staff:
            messages.info(request, 'Staff already exists')
            return HttpResponse('Staff already exists')
        else:
            staff = Staff.objects.create(
                first_name=recruit.first_name,
                middle_name=recruit.middle_name,
                last_name=recruit.last_name,
                email=recruit.email,
                mobile_number=recruit.mobile_number,
                status=StaffStatusChoices.ACTIVE
            )
            staff.save()
            recruit.delete()
            messages.success(request, f'{recruit.full_name} is now staff.')
            return HttpResponse("deleted")

def job_details(request, pk):
    recruitment = Recruitment.objects.get(pk=pk)
    return render(request, 'partials/job-details.html', {'recruitment': recruitment})

def send_application(request, pk):
    vac = Vacancy.objects.get(pk=pk)
    if request.method == 'POST':
        Application(
            first_name=request.POST['fname'],
            middle_name=request.POST['mname'],
            last_name=request.POST['lname'],
            email=request.POST['aemail'],
            mobile_number=request.POST['mnumber'],
            message=request.POST['cv-message'],
            resume=request.FILES.get('cv'),
            applied_position=vac
        ).save()
        return JsonResponse({"message": "application sent successifully"})
    return JsonResponse({"erro": "application not sent"})


