from django.shortcuts import render


def company_base(request):
    return render(request, template_name="bases/company_base.html")


def dashboard(request):
    return render(request, template_name="Company/dashboard.html")
