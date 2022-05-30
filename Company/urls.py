from django.urls import path

from Company import views

urlpatterns = [
    path('base', views.company_base),
    path('dashboard', views.dashboard, name="company_dashboard")
]
