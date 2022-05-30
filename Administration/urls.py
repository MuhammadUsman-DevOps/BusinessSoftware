from django.urls import path

from Administration import views

urlpatterns = [
    path('admin-base/', views.admin_base, name="admin_base"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('users/', views.users_view, name="users"),
    path('users/create', views.create_user, name="create_user"),

    path('roles/', views.roles_view, name="roles"),
    path('roles/create', views.create_role, name="create_role"),
    path('roles/<int:role_id>/edit', views.edit_role, name="edit_role"),
    path('roles/<int:role_id>/delete', views.delete_role, name="delete_role"),

    path('cms/pages/', views.pages_view, name="pages"),

    path('cms/faqs/', views.faqs_view, name="faqs"),

    path('cms/announcements/', views.announcements_view, name="announcements"),

    path('payment-methods/', views.payment_methods, name="payment_methods"),

    path('invoices/', views.invoices_view, name="invoices"),
]
