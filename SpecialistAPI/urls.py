from django.urls import path
from . import views

urlpatterns = [
    path('<int:k>/', views.index, name='index')
]