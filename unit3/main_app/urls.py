from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_widget/', views.add_widget, name='add_widget'),
    path('delete/<int:id>', views.widgets_delete, name='widgets_delete'),
]
