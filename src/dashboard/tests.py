from django.test import TestCase

from .views import *

class DashboardTest(TestCase):
    
    def test_authenticated_user(self):
        self.assertTrue(self.client.user.is_authenticated, True)
