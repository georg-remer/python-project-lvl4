from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserList.as_view(), name='list'),
    path('create/', views.UserCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.UserUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.UserDelete.as_view(), name='delete'),
]
