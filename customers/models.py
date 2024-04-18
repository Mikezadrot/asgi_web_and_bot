from django.db import models
import uuid
from django.contrib.auth.models import User
from departments.models import Department

class Telegram_user(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, editable=True, verbose_name="UUID", default=uuid.uuid4)
    username = models.CharField(max_length=255, null=True, blank=True)
    id_telegram = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    locale = models.CharField(max_length=255, null=True, blank=True, default="en", )
    confirmed_user = models.BooleanField(default=False, editable=True, null=True,)

    def __str__(self):
        return str(self.username)


class Customer(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, editable=True, verbose_name="UUID", default=uuid.uuid4)
    telegram_user = models.ForeignKey(Telegram_user, on_delete=models.DO_NOTHING, null=True, blank=True)

    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, blank=True)
    speciality = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    description = models.TextField(null=True, blank=True, editable=True)

    def __str__(self):
        return str(self.name)

