import pathlib

from .system_settings import SystemSettings

BASE_PATH = pathlib.Path(__file__).resolve().parent.parent

class SettingsGuaranteeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        settings_exists = SystemSettings.objects.exists()
        if settings_exists:
            response = self.get_response(request)
            return response
        else:
            settings = SystemSettings.objects.create(
                company_name="Django Hrm",
                company_logo=None,
                use_name=True,
                company_address="Not set",
                company_email="Not set",
                company_mobile_number=None,
                company_zip="Not set",
                currency="Not set"
            )
            settings.save()
            response = self.get_response(request)
            return response
