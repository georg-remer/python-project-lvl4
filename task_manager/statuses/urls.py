from django.urls import path

from . import views

urlpatterns = [
    path('', views.StatusList.as_view(), name='list'),
    path('create/', views.StatusCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.StatusUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.StatusDelete.as_view(), name='delete'),
]
