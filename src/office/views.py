from django.shortcuts import HttpResponse
from django.views.generic import DetailView, TemplateView, ListView
from django.db.models import Q

from .attendance import Attendance
from .hrd import Payroll

class AttendanceView(TemplateView):
    queryset = Attendance.objects.all()
    template_name = 'pages/attendance.html'
    object_name = 'attendance'


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

