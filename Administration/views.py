from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Administration.models import Role, Profile


def admin_base(request):
    return render(request, template_name="bases/admin_base.html")


def dashboard(request):
    return render(request, template_name="Administration/dashboard.html")


def users_view(request):
    return render(request, template_name="Administration/users/users.html")


def create_user(request):
    roles = Role.objects.all()
    if request.method == "POST":
        user = User.objects.create(
            username=request.POST.get("email_address"),
            email=request.POST.get("email_address"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            is_active=True,
        )
        user.set_password(request.POST.get("password"))
        if request.POST.get("user_role") == "Admin":
            user.is_staff = True
        user.save()
        print("user: ", user)
        profile = Profile.objects.create(
            user=user,
            # profile_picture=request.POST["profile_picture"],
            phone_number=request.POST.get("phone_number"),
            role=roles.get(role_name=request.POST.get("user_role")),

        )
        profile.save()
        messages.success(request, "User Created Successfully!")
    context = {
        "roles": roles
    }
    return render(request, template_name="Administration/users/create.html", context=context)


def roles_view(request):
    roles = Role.objects.all()
    context = {
        "roles": roles
    }
    return render(request, template_name="Administration/roles/roles.html", context=context)


def create_role(request):
    if request.method == "POST":
        subscription_required = False
        disable_login = False
        if request.POST.get("subscription_required") == "on":
            subscription_required = True
        if request.POST.get("disable_login") == "on":
            disable_login = True

        role = Role.objects.create(
            role_name=request.POST.get("role_name"),
            subscription_required=subscription_required,
            disable_login=disable_login,
        )
        role.save()
        messages.success(request, "Role Created Successfully!")
    return render(request, template_name="Administration/roles/create.html")


def edit_role(request, role_id):
    role = Role.objects.get(pk=role_id)
    if request.method == "POST":
        subscription_required = False
        disable_login = False
        if request.POST.get("subscription_required") == "on":
            subscription_required = True
        if request.POST.get("disable_login") == "on":
            disable_login = True

        role.role_name = request.POST.get("role_name")
        role.subscription_required = subscription_required
        role.disable_login = disable_login
        role.save()
        messages.success(request, "Role Updated Successfully!")
    context = {
        "role": role
    }
    return render(request, template_name="Administration/roles/create.html", context=context)


def delete_role(request, role_id):
    Role.objects.get(pk=role_id).delete()
    return redirect("roles")


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
