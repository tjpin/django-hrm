from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from staff.models import Staff


class SystemPermissions(Permission):

    @staticmethod
    def new_permission(code, name, model):
        Permission.objects.create(
            codename=code, 
            name=name, 
            content_type=ContentType.objects.get_for_model(model)
        ).save()

    def can_create_staff(self):
        return new_permission('can_view_staff', 'Can View Staffs', Staff)

    def can_update_staff(self):
        return new_permission('can_view_staff', 'Can View Staffs', Staff)
