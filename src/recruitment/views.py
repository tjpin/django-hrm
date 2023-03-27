from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import DetailView, ListView

from .models import Application, Recruit, Recruitment, Vacancy

class RecruitmentHomeView(ListView):
    # queryset = Recruitment.objects.select_related('vacancy')
    queryset = Vacancy.objects.all().order_by('application_deadline')
    template_name = 'pages/recruitment.html'
    context_object_name = 'recruitments'

class CareerView(ListView):
    queryset = Vacancy.objects.all().order_by('application_deadline')
    context_object_name = 'careers'
    template_name = 'pages/career.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['applications'] = Application.objects.all().order_by('date_applied')
        context['recruits'] = Recruit.objects.all()
        context['recruitments'] = Recruitment.objects.all()
        return context

def job_details(request, pk):
    vacancy = Vacancy.objects.get(pk=pk)
    return render(request, 'partials/job-details.html', {'vacancy': vacancy})

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


