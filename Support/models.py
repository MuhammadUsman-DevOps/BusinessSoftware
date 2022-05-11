from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class SupportTeam(models.Model):
    team_name = models.CharField(max_length=500)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class TeamUser(models.Model):
    team = models.ForeignKey(SupportTeam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class IssueType(models.Model):
    issue_title = models.CharField(max_length=500)
    category = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    team = models.ForeignKey(SupportTeam, on_delete=models.CASCADE)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SuggestedSolution(models.Model):
    title = models.CharField(max_length=1000)
    description = RichTextField()
    order = models.IntegerField()

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SupportTicket(models.Model):
    TICKET_STATUS = [
        ('new', 'New'),
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    CATEGORIES = [
        ('support', 'Support'),
        ('sale', 'Sale'),
        ('tech', 'Technical'),

    ]
    subject = models.CharField(max_length=1000)
    description = RichTextField()
    attachment = models.FileField(upload_to="tickets/", null=True, blank=True)
    status = models.CharField(max_length=250, choices=TICKET_STATUS)
    category = models.CharField(max_length=250, choices=CATEGORIES)
    resolution_hr = models.CharField(max_length=50,null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    auto_assign = models.BooleanField(default=True)
    owner = models.EmailField()
    assignee = models.ForeignKey(SupportTeam, on_delete=models.CASCADE)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SupportTicketReply(models.Model):
    reply = RichTextField()
    ticket = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
