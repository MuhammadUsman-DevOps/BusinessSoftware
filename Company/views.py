from django.shortcuts import render


def company_base(request):
    return render(request, template_name="bases/company_base.html")


def dashboard(request):
    return render(request, template_name="Company/dashboard.html")


def company_settings(request):
    return render(request, template_name="Company/settings.html")


def add_counter_party(request):
    return render(request, template_name="Company/counter_party/add_counter_party.html")


def add_investor(request):
    return render(request, template_name="Company/investors/add_investors.html")


def all_investors(request):
    return render(request, template_name="Company/investors/all_investors.html")


def all_counter_parties(request):
    return render(request, template_name="Company/counter_party/counter_parties.html")


def add_bank_account(request):
    return render(request, template_name="Company/bank_accounts/add_bank_account.html")


def all_bank_accounts(request):
    return render(request, template_name="Company/bank_accounts/bank_accounts.html")
