from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    APPLICANT = 1
    EMPLOYER = 2

    ROLE_CHOICES = [
        (APPLICANT, 'Applicant'),
        (EMPLOYER, 'Employer')
    ]
    role = models.PositiveSmallIntegerField(default=APPLICANT, choices=ROLE_CHOICES)
