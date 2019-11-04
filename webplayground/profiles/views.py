from django.shortcuts import render
from django.views.generic import ListView, DetailView
from registration.models import Profile
from django.shortcuts import get_object_or_404

# Create your views here.

class ProfileList(ListView):
    model=Profile
    template_name='profiles/profiles_list.html'
    paginate_by=3

class ProfileDetail(DetailView):
    model=Profile
    template_name='profiles/profiles_detail.html'

#Se recupera el username pasado en el path
    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])