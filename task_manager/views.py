from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = _('Logged in successfully.')


class LogoutView(LogoutView):
    pass
