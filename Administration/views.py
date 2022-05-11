from django.shortcuts import render


def admin_base(request):
    return render(request, template_name="bases/admin_base.html")


def dashboard(request):
    return render(request, template_name="Administration/dashboard.html")


def users_view(request):
    return render(request, template_name="Administration/users/users.html")


def create_user(request):
    return render(request, template_name="Administration/users/create.html")


def roles_view(request):
    return render(request, template_name="Administration/roles/roles.html")


def create_role(request):
    return render(request, template_name="Administration/roles/create.html")


def pages_view(request):
    return render(request, template_name="Administration/cms/pages/pages.html")


def faqs_view(request):
    return render(request, template_name="Administration/cms/faqs/faqs.html")


def announcements_view(request):
    return render(request, template_name="Administration/cms/announcements/announcements.html")


def payment_methods(request):
    return render(request, template_name="Administration/payments/payment-methods.html")


def invoices_view(request):
    return render(request, template_name="Administration/payments/invoices.html")
