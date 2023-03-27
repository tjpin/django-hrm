from django.urls import path
from django.views.decorators.cache import cache_page

from .views import AttendanceView, PayrollView

urlpatterns = [
    path('', AttendanceView.as_view(), name='attendance'),
    path('payroll/', cache_page(60*15)(PayrollView.as_view()), name='payroll')
]
