from django.urls import path

from . import views

urlpatterns = [
    path('', views.LabelList.as_view(), name='list'),
    path('create/', views.LabelCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.LabelUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.LabelDelete.as_view(), name='delete'),
]
