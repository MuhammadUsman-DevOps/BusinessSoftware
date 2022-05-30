from django.urls import path

from WSITE import views

urlpatterns = [

    path('base', views.site_base),
    path('signup/', views.company_signup, name="company_signup"),
    path('signin/', views.company_signin, name="company_signin"),

]
