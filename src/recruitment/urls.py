from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (CareerView, job_details, send_application, RecruitmentHomeView)


urlpatterns = [
    # path('', CareerView.as_view(), name='career'),
    path('', cache_page(60*15)(RecruitmentHomeView.as_view()), name='recruitment'),
    path('<int:pk>/', job_details, name='vacancy'),
    path('application/<int:pk>/', send_application, name='application'),
    # path('<int:pk>/', CareerDetailViiew.as_view(), name='vacancy'),
]

