from django.urls import path

from Company import views

urlpatterns = [
    path('base', views.company_base),
    path('dashboard', views.dashboard, name="company_dashboard"),
    path('settings/', views.company_settings, name="company_settings"),

    path('investors/add', views.add_investor, name="add_investor"),
    path('investors/', views.all_investors, name="all_investors"),

    path('counter-parties/add', views.add_counter_party, name="add_counter_party"),
    path('counter-parties/', views.all_counter_parties, name="all_counter_parties"),


    path('bank-accounts/add', views.add_bank_account, name="add_bank_account"),
    path('bank-accounts/', views.all_bank_accounts, name="all_bank_accounts"),
]
