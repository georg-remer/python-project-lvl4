"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from task_manager import views

urlpatterns = [
    path('', view=views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('users/', include(('task_manager.users.urls', 'users'), namespace='users')),
    path('statuses/', include(('task_manager.statuses.urls', 'statuses'), namespace='statuses')),
    path('tasks/', include(('task_manager.tasks.urls', 'tasks'), namespace='tasks')),
    path('labels/', include(('task_manager.labels.urls', 'labels'), namespace='labels')),
]
