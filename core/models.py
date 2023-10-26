import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Member(models.Model):
    MEMBERSHIP_BRONZE = 'Bronze'
    MEMBERSHIP_SILVER = 'Silver'
    MEMBERSHIP_GOLD = 'Gold'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, MEMBERSHIP_BRONZE),
        (MEMBERSHIP_SILVER, MEMBERSHIP_SILVER),
        (MEMBERSHIP_GOLD, MEMBERSHIP_GOLD),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
