from django.db import models
from project_m_n_e_service.config.base_model import BaseModel

# Create your models here.

class Project(BaseModel):
    id = models.UUIDField(primary_key=True, unique=True)
    name = models.CharField(max_length=500)
    
    

    class Meta:
        db_table = "project"
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name
