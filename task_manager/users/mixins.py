from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class SelfCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object() == self.request.user

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = _(
            'You do not have permission to modify another user.'
        )
        self.permission_denied_url = reverse_lazy('users:list')
        return super().dispatch(request, *args, **kwargs)
