from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import User


class Job(models.Model):
    title = models.CharField(max_length=255, default='')
    company_name = models.CharField(max_length=255, default='')
    location = models.CharField(max_length=255, default='')
    contact_info = models.CharField(max_length=255, default='')
    date_added = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, default='')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})
