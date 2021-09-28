from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import PermissionDeniedMixin, SuccessMessageDeleteMixin

from .forms import UserForm
from .mixins import SelfCheckMixin


class UserList(ListView):
    template_name = 'users/list.html'
    model = get_user_model()


class UserCreate(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = _('User was successfully created')


class UserUpdate(PermissionDeniedMixin, SelfCheckMixin, SuccessMessageMixin, UpdateView):
    template_name = 'users/update.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('users:list')
    success_message = _('User was successfully updated')


class UserDelete(PermissionDeniedMixin, SelfCheckMixin, SuccessMessageDeleteMixin, DeleteView):
    template_name = 'users/delete.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('users:list')
    success_message = _('User was successfully deleted')
