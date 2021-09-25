from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class SelfCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object() == self.request.user

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = _('You do not have permission to modify another user.')
        self.permission_denied_url = reverse_lazy('users:list')
        return super().dispatch(request, *args, **kwargs)


class PermissionDeniedMixin:
    permission_denied_message = ''
    permission_denied_url = reverse_lazy('index')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(self.permission_denied_url)
