from django.urls import path
from .views import LoginView, DashboardView

urlpatterns = [
    path('', LoginView.as_view(), name='login'), #this url config follow session/
    path('dashboard/', DashboardView.as_view(), name='dashboard'),#this url config follow session/dashbaord
]
