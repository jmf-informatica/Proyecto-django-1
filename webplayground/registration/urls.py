from django.urls import path
from .views import RegistroUsuario, ProfileUpdate, EmailUpdate

urlpatterns=[
    path('registro/', RegistroUsuario.as_view(),name='registro'),
    path('profile/', ProfileUpdate.as_view(),name='profile'),
    path('profile/email', EmailUpdate.as_view(),name='profile_email'),
]


