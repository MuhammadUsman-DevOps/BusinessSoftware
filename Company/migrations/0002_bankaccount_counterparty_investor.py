# Generated by Django 3.2.14 on 2022-07-17 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investor_name', models.CharField(max_length=1500)),
                ('short_name', models.CharField(max_length=500)),
                ('reporting_currency', models.CharField(max_length=25)),
                ('legal_form', models.CharField(max_length=500)),
                ('incorporate_date', models.DateField()),
                ('investor_type', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.company')),
            ],
        ),
        migrations.CreateModel(
            name='CounterParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter_party_name', models.CharField(max_length=1500)),
                ('short_name', models.CharField(max_length=500)),
                ('countery_party_type', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.company')),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=1500)),
                ('short_name', models.CharField(max_length=500)),
                ('account_type', models.CharField(max_length=250)),
                ('currency', models.CharField(max_length=25)),
                ('account_number', models.CharField(max_length=100)),
                ('IBAN', models.CharField(max_length=100)),
                ('swift_code', models.CharField(max_length=100)),
                ('BIC', models.CharField(max_length=100)),
                ('address_line', models.CharField(max_length=1500)),
                ('investor_type', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.company')),
            ],
        ),
    ]