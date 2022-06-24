from django.db import models
from config.base_model import BaseModel

# Create your models here.


class ProjectCategory(BaseModel):
    name = models.CharField(max_length=4000)
    short_name = models.CharField(max_length=4000, null=True, blank=True)

    class Meta:
        db_table = "project_category"

    managed = True
    verbose_name = "Project Category"
    verbose_name_plural = "Project Categoriess"

    def __str__(self):
        self.name


class ProjectSubCategory(BaseModel):
    name = models.CharField(max_length=300)
    short_name = models.CharField(max_length=300, null=True, blank=True)
    category = models.ForeignKey("ProjectCategory", on_delete=models.DO_NOTHING)
    sub_category_of = models.ForeignKey(
        "ProjectSubCategory",
        verbose_name="sub_category_of",
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        self.name

    class Meta:
        db_table = "project_sub_category"
        managed = True
        verbose_name = "ProjectSubCategory"
        verbose_name_plural = "ProjectSubCategorys"


class Project(BaseModel):
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=8000, null=True, blank=True)
    description = models.TextField(max_length=100000, null=True, blank=True)
    estimate_time_line = models.IntegerField(null=True, blank=True)
    project_category = models.ForeignKey(
        "ProjectSubCategory", null=True, blank=True,on_delete=models.DO_NOTHING
    )

    class Meta:
        db_table = "project"
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name


class ProjectDeliverable(BaseModel):
    deliverable = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    planned_start_date = models.DateTimeField(null=True, blank=True)
    actual_start_date = models.DateTimeField(null=True, blank=True)
    planned_end_date = models.DateTimeField(null=True, blank=True)
    actual_end_date = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey("Project", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "project_deliverable"
        managed = True
        verbose_name = "Project Deliverable"
        verbose_name_plural = "Project Deliverables"

    def __str__(self):
        self.deliverable
