from src.dashboard.system_settings import SystemSettings


def create_settings(request, logo, useName):
    sys = SystemSettings.objects.update_or_create(
        company_name=request.POST.get('company_name'),
        company_logo=logo,
        use_name=True if useName == 'on' else False,
        company_address=request.POST.get('company_address'),
        company_email=request.POST.get('company_email'),
        company_mobile_number=request.POST.get('company_mobile_number'),
        company_zip=request.POST.get('company_zip'),
        currency=request.POST.get('currency')
    )
