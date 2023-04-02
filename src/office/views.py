from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.decorators.http import require_http_methods 
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, FormView
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages

from .attendance import Attendance
from .hrd import Payroll
from .forms import AttendanceForm, DataExportForm, PayrollForm
from utils.data_export import AttendanceResource
from utils.choice_helper import ExportChoices

class AttendanceView(ListView, FormView):
    queryset = Attendance.objects.all().filter(date=timezone.now().date()).order_by('-date')
    template_name = 'pages/attendance.html'
    context_object_name = 'attendances'
    form_class = DataExportForm
    
    def get_queryset(self, **kwargs):
        _all = 'all'
        qs = self.request.GET.get('aq')
        qdate = self.request.GET.get('dq')
        if qs == _all.lower():
            return Attendance.objects.select_related('staff').order_by('-date')
        if qs is None and qdate is None:
            return self.queryset
        if qdate:
            queryset = Attendance.objects.filter(date=qdate).order_by('-date')
            return queryset
        if qs and qdate:
            queryset = Attendance.objects.select_related('staff').filter(
                Q(staff__first_name__icontains=qs) | Q(staff__last_name__icontains=qs) |
                Q(staff__staff_number__icontains=qs) & Q(date__iexact=qdate)
            ).order_by('-date')
        if not qdate and qs is not None:
            queryset = Attendance.objects.filter(
                Q(staff__first_name__icontains=qs) | Q(staff__last_name__icontains=qs) |
                Q(staff__staff_number__icontains=qs)
            ).order_by('-date')
            return queryset
    
    def post(self, request, **kwargs):
        now = timezone.now().date()
        date = request.POST.get('date-selected')
        if date:
            qs = self.get_queryset().filter(date=date).order_by('-date')
        else:
            qs = self.get_queryset().filter(date=now).order_by('-date')
        dataset = AttendanceResource().export(qs)
        formats = request.POST.get('export_format')
        if formats == ExportChoices.XLSX:
            exp = dataset.xlsx
        elif formats == ExportChoices.XLS:
            exp = dataset.xls
        elif formats == ExportChoices.CSV:
            exp = dataset.csv
        else:
            exp = dataset.json
        response = HttpResponse(exp, content_type='{}'.format(formats))
        response['Content-Disposition'] = "attachment; filename={}.{}".format(now, formats)
        messages.success(request, 'Data downloding...')
        return response

@csrf_exempt
def update_attendance(request, pk):
    obj = Attendance.objects.get(pk=pk)
    form = AttendanceForm(request.POST or None, instance=obj)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/office/')
        else:
            print()
            print(form.errors)
    return render(request, 'partials/attendance_update.html', {'form': form, 'atd': obj})

class PayrollView(ListView):
    queryset = Payroll.objects.select_related('staff').order_by('-month')
    template_name = 'pages/payroll.html'
    context_object_name = 'payrolls'
    
    def get_queryset(self):
        query = self.request.GET.get('qs')
        if query:
            filtered = Payroll.objects.select_related('staff').filter(
                Q(staff__first_name__icontains=query) | Q(staff__last_name__icontains=query) |
                Q(transaction_id__icontains=query) | Q(month__icontains=query) | 
                Q(pay_date__icontains=query) | Q(status=query)
            )
            return filtered
        return self.queryset

@require_http_methods(["GET", "POST"])
def payroll_add(request):
    form = PayrollForm()
    if request.method == "POST":
        form = PayrollForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('payroll')
        else:
            print(form.errors)
            return render(request, 'partials/payrol-add.html', {'form': form})
    return render(request, 'partials/payrol-add.html', {'form': form})
