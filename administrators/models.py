from django.db import models
import uuid
from departments.models import Department
from django.contrib.auth.models import User


class Administrator(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, editable=True, verbose_name="UUID", default=uuid.uuid4)
    name = models.CharField(max_length=255, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,
                                related_name="administrator")
    administrator_department = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return str(self.name)