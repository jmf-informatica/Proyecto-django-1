from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistroForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    def clean_email(self): # Validacion del campo email.
        # Función que verifica si el email ya se encuentra registrado en la DB
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya se encuentra registrado.')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=[
        'avatar','bio','link'
    ]
        widgets={
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Escriba su biografia'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3','placeholder':'Enlace'}),

        }

        labels={
            'avatar':'',
            'bio':'',
            'link':'',
        }

class EmailForm(forms.ModelForm):
    email=forms.EmailField(required=True,help_text='requerido 254 caracteres como maximo y debe ser un email valido'),
    
    class Meta:
        model=User
        fields=[
            'email'
        ]
    
    def clean_email(self): # Validacion del campo email.
        # Función que verifica si el email ya se encuentra registrado en la DB
        email=self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Este email ya se encuentra registrado.')
        return email

    