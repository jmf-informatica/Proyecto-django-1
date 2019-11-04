from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
# Create your tests here.


# Test que evalua si se crea un perfil por cada usuario registrado ( ejecutar test con python manage.py test registration )
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('prueba','prueba@prueba.com','Test1234')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='prueba').exists()
        self.assertEqual(exists,True)