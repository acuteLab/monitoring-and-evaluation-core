from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    created_by = models.CharField(max_length=4000,null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
