from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('src.dashboard.urls')),
    path('admin/', admin.site.urls),
    path('staffs/', include('src.staff.urls')),
    path('documents/', include('src.record.urls')),
    path('office/', include('src.office.urls')),
    path('recruitment/', include('src.recruitment.urls')),

    path('api/', include('api.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler403 = 'utils.request_errors.error_403'
handler404 = 'utils.request_errors.error_404'
# handler403 = 'src.staff.views.error_403'
# handler404 = 'src.staff.views.error_404'
