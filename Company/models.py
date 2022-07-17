from pyexpat import model
from statistics import mode
from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=1500)
    phone_number = models.CharField(max_length=250)
    email_address = models.EmailField()
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100)
    industry = models.CharField(max_length=500)
    total_employees = models.IntegerField(null=True, blank=True)
    turn_over = models.IntegerField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CompanyStaff(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    user_role_at_company = models.CharField(max_length=200, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




class CounterParty(models.Model):
    counter_party_name = models.CharField(max_length=1500)
    short_name = models.CharField(max_length=500)
    countery_party_type = models.CharField(max_length=500)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




class Investor(models.Model):
    investor_name = models.CharField(max_length=1500)
    short_name = models.CharField(max_length=500)
    reporting_currency = models.CharField(max_length=25)
    legal_form = models.CharField(max_length=500)
    incorporate_date = models.DateField()
    investor_type = models.CharField(max_length=500)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




class BankAccount(models.Model):
    account_name = models.CharField(max_length=1500)
    short_name = models.CharField(max_length=500)
    account_type = models.CharField(max_length=250)
    currency = models.CharField(max_length=25)
    account_number = models.CharField(max_length=100)
    IBAN = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=100)
    BIC = models.CharField(max_length=100)
    address_line = models.CharField(max_length=1500)
    investor_type = models.CharField(max_length=500)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
