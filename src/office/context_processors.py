from .models import Department

from src.dashboard.system_settings import SystemSettings
from src.dashboard.forms import SettingsForm

def departments(request):
    system_settings = SystemSettings.objects.first()
    settings_form = SettingsForm(request.POST or None, request.FILES or None, instance=system_settings)
    context =  {
        'departments': Department.objects.all(),
        'system_settings': system_settings,
        'settings_form': settings_form
        }

    return context
