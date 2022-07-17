from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from Company.models import Company


class Role(models.Model):
    role_name = models.CharField(max_length=100)
    subscription_required = models.BooleanField(default=False)
    disable_login = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    # TODO : Permission

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="users", null=True, blank=True, default="avatar.jpg")
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Subscription(models.Model):
    subscription_name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to="subscriptions/", null=True, blank=True, default="subscription.png")

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SubscriptionPlan(models.Model):
    PLAN_DURATION = [
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
    ]
    plan_name = models.CharField(max_length=1000)
    plan_code = models.CharField(max_length=250)
    price = models.FloatField()
    frequency = models.IntegerField(null=True, blank=True, default=1)
    duration = models.CharField(choices=PLAN_DURATION, max_length=50)
    free_trial_days = models.IntegerField(null=True, blank=True, default=0)
    display_order = models.IntegerField()

    is_recommended = models.BooleanField(default=False)
    is_free_plan = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class PlanFeature(models.Model):
    FEATURE_TYPE = [
        ('qty', 'Quantity'),
        ('txt', 'Text'),
        ('bol', 'Boolean (True/False)'),
    ]
    feature_name = models.CharField(max_length=1000)
    feature_caption = models.CharField(max_length=1000, null=True, blank=True)
    type = models.CharField(choices=FEATURE_TYPE, max_length=50)
    type_value = models.CharField(max_length=1000, help_text="If Boolean, input True or False.")
    limit_reached_message = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class PurchasedSubscription(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Announcement(models.Model):
    title = models.CharField(max_length=1000)
    content = RichTextField()
    picture = models.ImageField(upload_to="announcements/", null=True, blank=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    show_in_page = models.CharField(max_length=500, null=True, blank=True)
    share_to_roles = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    is_public = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class FAQ(models.Model):
    question = RichTextField()
    answer = RichTextField()

    published = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Testimonial(models.Model):
    author = models.CharField(max_length=500)
    job_title = models.CharField(max_length=250, null=True, blank=True)
    picture = models.ImageField(upload_to="testimonials/", default="avatar.jpg", null=True, blank=True)
    review = RichTextField(null=True, blank=True)
    rating = models.FloatField()

    published = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class GeneralSettings(models.Model):
    site_name = models.CharField(max_length=1000, null=True, blank=True)
    logo_dark = models.ImageField(upload_to="site/logo", null=True, blank=True)
    logo_white = models.ImageField(upload_to="site/logo", null=True, blank=True)
    favicon = models.ImageField(upload_to="site/logo", null=True, blank=True)
    footer_text = models.TextField(null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)

    google_analytics_ID = models.TextField(null=True, blank=True)
    google_tag_manager = models.TextField(null=True, blank=True)
    supported_languages = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    currency_code = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class UserSetting(models.Model):
    default_user_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    two_factor_ath = models.BooleanField(default=False)
    confirm_email_on_registration = models.BooleanField(default=False)
    enable_cookie_consent = models.BooleanField(default=False)
    cookie_consent_text = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class PaymentSetting(models.Model):
    gateway_name = models.CharField(max_length=500)
    live_public_key = models.TextField()
    live_secret_key = models.TextField()
    live_webhook = models.TextField(null=True, blank=True)
    demo_public_key = models.TextField()
    demo_secret_key = models.TextField()
    demo_webhook = models.TextField(null=True, blank=True)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ActivityLog(models.Model):
    log = models.TextField()
    model = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)