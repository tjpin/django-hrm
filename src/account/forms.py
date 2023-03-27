from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import AccountUser


class AccountUserCreationForm(UserCreationForm):
    class Meta:
        model = AccountUser
        fields = "__all__"


class AccountUserChangeForm(UserChangeForm):
    class Meta:
        model = AccountUser
        fields = "__all__"

