from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import TaskForm
from .mixins import CheckCreatedByMixin
from .models import Task
from task_manager.mixins import AuthRequiredMixin, PermissionDeniedMixin


class TaskList(PermissionDeniedMixin, AuthRequiredMixin, ListView):
    template_name = 'tasks/list.html'
    model = Task


class TaskCreate(PermissionDeniedMixin, AuthRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'tasks/create.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')
    success_message = _('Task was successfully created.')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskUpdate(PermissionDeniedMixin, AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'tasks/update.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')
    success_message = _('Task was successfully updated.')


class TaskDelete(PermissionDeniedMixin, AuthRequiredMixin, CheckCreatedByMixin, SuccessMessageMixin, DeleteView):
    template_name = 'tasks/delete.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')
    success_message = _('Task was successfully deleted.')


class TaskDetail(PermissionDeniedMixin, AuthRequiredMixin, SuccessMessageMixin, DetailView):
    template_name = 'tasks/detail.html'
    model = Task