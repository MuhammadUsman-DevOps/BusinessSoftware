# Generated by Django 3.2.13 on 2022-05-09 18:44

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', ckeditor.fields.RichTextField()),
                ('answer', ckeditor.fields.RichTextField()),
                ('published', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('logo_dark', models.ImageField(blank=True, null=True, upload_to='site/logo')),
                ('logo_white', models.ImageField(blank=True, null=True, upload_to='site/logo')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='site/logo')),
                ('footer_text', models.TextField(blank=True, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('google_analytics_ID', models.TextField(blank=True, null=True)),
                ('google_tag_manager', models.TextField(blank=True, null=True)),
                ('supported_languages', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_code', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gateway_name', models.CharField(max_length=500)),
                ('live_public_key', models.TextField()),
                ('live_secret_key', models.TextField()),
                ('live_webhook', models.TextField(blank=True, null=True)),
                ('demo_public_key', models.TextField()),
                ('demo_secret_key', models.TextField()),
                ('demo_webhook', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=1000)),
                ('feature_caption', models.CharField(blank=True, max_length=1000, null=True)),
                ('type', models.CharField(choices=[('qty', 'Quantity'), ('txt', 'Text'), ('bol', 'Boolean (True/False)')], max_length=50)),
                ('type_value', models.CharField(help_text='If Boolean, input True or False.', max_length=1000)),
                ('limit_reached_message', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100)),
                ('subscription_required', models.BooleanField(default=False)),
                ('disable_login', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, default='subscription.png', null=True, upload_to='subscriptions/')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=1000)),
                ('plan_code', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('frequency', models.IntegerField(blank=True, default=1, null=True)),
                ('duration', models.CharField(choices=[('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=50)),
                ('free_trial_days', models.IntegerField(blank=True, default=0, null=True)),
                ('display_order', models.IntegerField()),
                ('is_recommended', models.BooleanField(default=False)),
                ('is_free_plan', models.BooleanField(default=False)),
                ('is_visible', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=500)),
                ('job_title', models.CharField(blank=True, max_length=250, null=True)),
                ('picture', models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to='testimonials/')),
                ('review', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('rating', models.FloatField()),
                ('published', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('two_factor_ath', models.BooleanField(default=False)),
                ('confirm_email_on_registration', models.BooleanField(default=False)),
                ('enable_cookie_consent', models.BooleanField(default=False)),
                ('cookie_consent_text', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('default_user_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administration.role')),
            ],
        ),
        migrations.CreateModel(
            name='PurchasedSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.company')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administration.subscription')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to='users')),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Administration.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', ckeditor.fields.RichTextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='announcements/')),
                ('starts_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
                ('show_in_page', models.CharField(blank=True, max_length=500, null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('share_to_roles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Administration.role')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField()),
                ('model', models.TextField()),
                ('action', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]