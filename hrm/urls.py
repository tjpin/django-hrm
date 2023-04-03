from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.apps import apps

urlpatterns = [
    path('', include('src.dashboard.urls')),
    path('system-admin/', admin.site.urls),
    path('staffs/', include('src.staff.urls')),
    path('documents/', include('src.record.urls')),
    path('office/', include('src.office.urls')),
    path('recruitment/', include('src.recruitment.urls')),

    path('api/', include('api.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'utils.request_errors.error_400'
handler404 = 'utils.request_errors.error_404'
handler403 = 'utils.request_errors.error_403'
handler500 = 'utils.request_errors.error_500'


system_settings = apps.get_model(app_label='dashboard.SystemSettings').objects.first()

admin.sites.AdminSite.site_header = system_settings.company_name
admin.sites.AdminSite.site_title = system_settings.company_name
admin.sites.AdminSite.index_title = system_settings.company_name
