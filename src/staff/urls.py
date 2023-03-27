from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', cache_page(60*15)(views.StaffHome.as_view()), name='staffs'),
    # path('staffs/', views.StaffHome.as_view(), name='all-staffs'),
    path('staffs/', views.get_staffs, name='all-staffs'),
    path('add/', views.CreateStaff.as_view(), name='new'),
    path('update/<int:pk>/', views.StaffUpdateView.as_view(), name='update'),
    # path('update/<int:pk>/', views.update, name='update'),
    path('<int:pk>/', views.staff_data, name='staff-data'),
    path('payroll/<int:pk>/', views.PayrollDetails.as_view(), name='staff-payroll'),
    path('delete/<int:pk>/', views.DeleteStaff.as_view(), name='delete'),
]