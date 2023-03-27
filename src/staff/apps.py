from django.apps import AppConfig


class StaffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.staff'
    verbose_name = "Staffs"

    # def ready(self):
    #     import staff.signals
