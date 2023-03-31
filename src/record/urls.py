from django.urls import path

from .import views

urlpatterns = [
    path('', views.DocumentView.as_view(), name='documents'),
    path('add-record/', views.add_record, name='add-record'),
    path('<int:id>/', views.document_details, name='document-details')
]

