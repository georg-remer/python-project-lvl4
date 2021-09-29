from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class CheckCreatedByMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().creator == self.request.user

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = _('A task can only be deleted by its author')
        self.permission_denied_url = reverse_lazy('tasks:list')
        return super().dispatch(request, *args, **kwargs)
