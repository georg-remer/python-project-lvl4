from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import LabelForm
from .models import Label
from task_manager.mixins import AuthRequiredMixin, PermissionDeniedMixin


class LabelList(PermissionDeniedMixin, AuthRequiredMixin, ListView):
    template_name = 'labels/list.html'
    model = Label


class LabelCreate(PermissionDeniedMixin, AuthRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'labels/create.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:list')
    success_message = _('Label was successfully created.')


class LabelUpdate(PermissionDeniedMixin, AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'labels/update.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:list')
    success_message = _('Label was successfully updated.')


class LabelDelete(PermissionDeniedMixin, AuthRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'labels/delete.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:list')
    success_message = _('Label was successfully deleted.')

    def delete(self, request, *args, **kwargs):
        if self.get_object().labels.all().exists():
            messages.error(self.request, _('Unable to delete label because it is in use.'))
            return redirect('labels:list')

        return super().delete(request, *args, **kwargs)
