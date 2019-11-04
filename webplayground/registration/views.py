from django.contrib.auth.models import User
from .forms import RegistroForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Profile
from .forms import ProfileForm

# Create your views here.

class RegistroUsuario(SuccessMessageMixin,CreateView):
    model=User
    template_name='registration/registro.html'
    form_class=RegistroForm
    success_url=reverse_lazy('login')
    success_message="Usuario&nbsp;<b>%(username)s</b>&nbsp;registrado correctamente. Ya puedes iniciar la sesión"


    def get_form(self,form_class=None):
        form=super(RegistroUsuario,self).get_form()
        #Modifica en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba un usuario'})
        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba su nombre'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba su apellido'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Escriba su email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Escriba una contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repita la contraseña'})

        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class=ProfileForm
    success_url=reverse_lazy('profile')
    template_name='registration/profile_form.html'

    def get_object(self):
        # Recupera el objeto que se va a editar
        profile,create = Profile.objects.get_or_create(user=self.request.user) 
        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class=EmailForm
    success_url=reverse_lazy('profile')
    template_name='registration/profile_email_form.html'

    def get_object(self):
        # Recupera el objeto que se va a editar
        return self.request.user

    def get_form(self,form_class=None):
        form=super(EmailUpdate,self).get_form()
        #Modifica en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Escriba su email', 'style':'width:80%;margin:0 auto;'})
        return form
    

    
