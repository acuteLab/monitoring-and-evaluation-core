from django.db import models


class BaseModel(models.Model):
    created_by = models.CharField(max_length=4000,null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
