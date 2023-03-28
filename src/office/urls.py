from django.urls import path
from django.views.decorators.cache import cache_page

from .views import AttendanceView, PayrollView, update_attendance

''' :cache_page(60*15) will store cached data for 15 mins'''

urlpatterns = [
    path('', AttendanceView.as_view(), name='attendance'),
    # path('', cache_page(60*15)(AttendanceView.as_view()), name='attendance'),
    path('payroll/', cache_page(60*15)(PayrollView.as_view()), name='payroll'),
    path('attendance-update/<pk>/', update_attendance, name='attendance-update')
]
