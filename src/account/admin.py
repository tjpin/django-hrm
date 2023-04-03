from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountUserChangeForm, AccountUserCreationForm, AccountUser


@admin.register(AccountUser)
class AccountUserAdmin(UserAdmin):
    add_form = AccountUserCreationForm
    form = AccountUserChangeForm
    model = AccountUser

    list_display = ('first_name', 'last_name', 'email', 'date_joined', 'is_staff', 'is_active', 'user_token')
    list_filter = ('email', 'is_staff', 'is_active')
    list_display_links = ('first_name', 'last_name', 'email')


    fieldsets = (
        (None, {"fields": ("first_name", "last_name", "mobile_number", "email", "password", "profile_picture")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name", "last_name", "mobile_number", "email", "profile_picture", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )

    search_fields = ("email", "first_name")
    ordering = ("email", "first_name")

