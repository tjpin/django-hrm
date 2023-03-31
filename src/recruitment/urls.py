from django.urls import path

from .views import (job_details, send_application, add_recruit, promote_recruit, RecruitmentHomeView)


urlpatterns = [
    # path('', CareerView.as_view(), name='career'),
    path('', RecruitmentHomeView.as_view(), name='recruitment'),
    # path('', cache_page(60*15)(RecruitmentHomeView.as_view()), name='recruitment'),
    path('add-recruit/', add_recruit, name='add-recruit'),
    path('<int:pk>/', job_details, name='vacancy'),
    path('recruit/<int:pk>/', promote_recruit, name='promote'),
    path('application/<int:pk>/', send_application, name='application'),
    # path('<int:pk>/', CareerDetailViiew.as_view(), name='vacancy'),
]

