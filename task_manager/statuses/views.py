from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import AuthRequiredMixin, PermissionDeniedMixin, SuccessMessageDeleteMixin

from .forms import StatusForm
from .models import Status


class StatusList(PermissionDeniedMixin, AuthRequiredMixin, ListView):
    template_name = 'statuses/list.html'
    model = Status


class StatusCreate(PermissionDeniedMixin, AuthRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'statuses/create.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list')
    success_message = _('Status was successfully created')


class StatusUpdate(PermissionDeniedMixin, AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'statuses/update.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list')
    success_message = _('Status was successfully updated')


class StatusDelete(PermissionDeniedMixin, AuthRequiredMixin, SuccessMessageDeleteMixin, DeleteView):
    template_name = 'statuses/delete.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list')
    success_message = _('Status was successfully deleted')

    def delete(self, request, *args, **kwargs):
        if self.get_object().status.all().exists():
            messages.error(self.request, _('Unable to delete status because it is in use'))
            return redirect('statuses:index')

        return super().delete(request, *args, **kwargs)
