from typing import Counter
from django.shortcuts import render
from django.contrib import messages
from Company.models import CounterParty, Company


def company_base(request):
    return render(request, template_name="bases/company_base.html")


def dashboard(request):
    return render(request, template_name="Company/dashboard.html")


def company_settings(request):
    return render(request, template_name="Company/settings.html")


def add_counter_party(request):
    if request.method == "POST":
        counter_party = CounterParty.objects.create(
            counter_party_name = request.POST.get("party_name"),
            short_name = request.POST.get("short_name"),
            countery_party_type = request.POST.get("counter_party_type"),
            country = request.POST.get("country"),
            city = request.POST.get("city"),
            state = request.POST.get("state"),
            zip_code = request.POST.get("zip_code"),
            company = Company.objects.get(user=request.user)
        
        )
        counter_party.save()
        messages.success(request,"Counter party added successfully!")
    return render(request, template_name="Company/counter_party/add_counter_party.html")



def all_counter_parties(request):
    company = Company.objects.get(user=request.user)
    counter_parties = CounterParty.objects.filter(company=company)
    context = {
        "counter_parties": counter_parties
    }
    return render(request, template_name="Company/counter_party/counter_parties.html", context=context)


def add_investor(request):
    return render(request, template_name="Company/investors/add_investors.html")


def all_investors(request):
    return render(request, template_name="Company/investors/all_investors.html")




def add_bank_account(request):
    return render(request, template_name="Company/bank_accounts/add_bank_account.html")


def all_bank_accounts(request):
    return render(request, template_name="Company/bank_accounts/bank_accounts.html")
