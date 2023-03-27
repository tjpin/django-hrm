from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.decorators.cache import cache_page

from .import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('refresh/', views.refresh, name='refresh'),

    path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('settings/', views.update_settings, name='settings'),

    path('add-training/', views.add_training, name='add-training'),
    path('add-appointment/', views.add_appointment, name='add-appointment'),
    path('add-announcement/', views.add_announcement, name='add-announcement'),
    
    path('department-staffs/<int:id>/', views.staffs_per_deparment, name='department-staffs'),
]