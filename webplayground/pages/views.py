from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import PageForm

# Create your views here.

class PageListView(ListView):
    model=Page
    
class PageDetailView(DetailView):
    model=Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model=Page
    form_class=PageForm
    success_url=reverse_lazy('pages:pages')


class PageUpdate(PermissionRequiredMixin,UpdateView):
    permission_required="pages.change_page"
    model=Page
    form_class=PageForm
    template_name_suffix='_update_form'
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

class PageDelete(PermissionRequiredMixin,DeleteView):
    permission_required="pages.delete_page"
    model = Page
    form_class=PageForm
    template_name_suffix='_delete_form'
    success_url=reverse_lazy('pages:pages')