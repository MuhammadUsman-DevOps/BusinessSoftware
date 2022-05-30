from django.shortcuts import render



def site_base(request):
    return render(request, template_name="bases/site_base.html")


def company_signup(request):
    return render(request, template_name="WSITE/company_signup.html")


def company_signin(request):
    return render(request, template_name="WSITE/company_signin.html")