from django.test import TestCase

from .models import AccountUser, AbstractBaseUser


class AccountUserTest(TestCase):
    def setUp(self):
        self.new_user = AccountUser(
            first_name='John',
            last_name='Doe',
            email='johndoe@test.py',
            is_superuser=True
        )
        self.new_user.save()
        self.user = AccountUser.objects.first()

    def test_class_base(self):
        self.assertTrue(issubclass(AccountUser, AbstractBaseUser))
    
    def test_is_adminuser(self):
        self.assertTrue(self.user.is_superuser, True)
    
    def test_username(self):
        self.assertTrue(self.user.email==self.user.get_username())
    

    

