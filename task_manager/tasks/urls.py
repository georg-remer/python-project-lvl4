from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='list'),
    path('create/', views.TaskCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.TaskUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.TaskDelete.as_view(), name='delete'),
    path('<int:pk>/', views.TaskDetail.as_view(), name='detail'),
]
