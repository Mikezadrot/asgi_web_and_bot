from django.db import models
import uuid
# Create your models here.


class Department(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, editable=True, verbose_name="UUID", default=uuid.uuid4)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)