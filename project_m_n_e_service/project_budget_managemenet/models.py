from django.db import models
from djmoney.models.fields import MoneyField
from config.base_model import BaseModel
from project_planning.models import Project



class ProjectBudget(BaseModel):
    budget = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'project_budget'
        managed = True
        verbose_name = 'Project Budget'
        verbose_name_plural = 'Project Budgets'
    
        def __str__(self):
           f"{self.project__name} {self.budget_name}"
           

class ProjectDeliverableBudget(BaseModel):
    project_deliverable = models.ForeignKey("project_planning.ProjectDeliverable", on_delete=models.DO_NOTHING)
    estimate_budget =  MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    actual_amount_used = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    
    

    class Meta:
        db_table = "project_deliverable_budget"
        managed = True
        verbose_name = "Project Deliverable Budget"
        verbose_name_plural = "Project Deliverable Budgets"

    def __str__(self):
        return f"{self.project_deliverable__deliverable}  {self.estimate_budget}"
