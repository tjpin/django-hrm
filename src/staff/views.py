from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Staff
from .forms import StaffRegistrationForm
from src.record.models import Document
from src.office.hrd import Payroll
from utils.mixins import AdminAccessAndLoginMixin


class StaffHome(AdminAccessAndLoginMixin, ListView):
    queryset = Staff.objects.all()
    template_name = 'pages/staffs.html'
    context_object_name = 'staffs'
    permission_required = 'staff.view_staff'

    def get_queryset(self):
        print()
        print(self.request.META)
        query = self.request.GET.get('q')
        if query:
            filtered = Staff.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query) |
                Q(mobile_number__icontains=query) | Q(staff_number__icontains=query) |
                Q(status__icontains=query) | Q(grade__grade__icontains=query) | Q(department__department__icontains=query) 
            )
            return filtered
        return self.queryset

class CreateStaff(AdminAccessAndLoginMixin, FormView):
    model = Staff
    form_class = StaffRegistrationForm
    success_url = "/staffs/"
    template_name = 'forms/staff_registration.html'
    permission_required = ('staff.add_staff', 'account.add_account_user')

    @csrf_exempt
    def form_valid(self, form):
        print(self.request.FILES)
        files = self.request.FILES.getlist('document')
        for file in files:
            doc = Document.objects.create(
                uploaded_by=self.request.user,
                document=file,
            )
            doc.save()
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class DeleteStaff(AdminAccessAndLoginMixin, DeleteView):
    model = Staff
    success_url = reverse_lazy('staffs')
    template_name = 'widgets/staff_confirm_delete.html'
    permission_required = 'staff.delete_staff'

class PayrollDetails(AdminAccessAndLoginMixin, DetailView):
    model = Payroll
    template_name = 'widgets/payslip-details.html'

    def get_context_data(self, **kwargs):
        context = super(PayrollDetails, self).get_context_data(**kwargs)
        context['staff'] = kwargs.get('object', None).staff
        print()
        print(context)
        return context

class StaffUpdateView(AdminAccessAndLoginMixin, UpdateView):
    template_name = 'forms/staff_update.html'
    form_class = StaffRegistrationForm

    def get_queryset(self):
        return Staff.objects.all()
    
    def get_success_url(self):
        return reverse('staffs')

def get_staffs(request):
    from office.models import Department
    staffs = Staff.objects.all()
    depts = {'department': {'depts': []}}
    for i in staffs.values():
        d = Department.objects.get(id=i["department_id"])
        depts['department']['depts'].append(d.department)
    data = serializers.serialize('json', staffs)
    return JsonResponse(depts, safe=False)

# @permission_required("staff.view_staff")
def staff_data(request, pk):
    staff = Staff.objects.get(pk=pk)
    return render(request, 'partials/staff-detail.html', {'staff': staff})
