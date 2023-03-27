from django.urls import path

from .import views

urlpatterns = [
    path('', views.DocumentView.as_view(), name='documents'),
    path('<int:id>/', views.document_details, name='document-details')
]
