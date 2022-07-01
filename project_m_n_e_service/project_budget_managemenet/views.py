from django.shortcuts import render
from .models import ProjectBudget as project_budget_table

# Create your views here.

class ProjectBudget:
    def __init__(self):
          pass
      
    def create_project_budget(request, project_budget_data):
        try:
            if project_budget_data:
                if type(project_budget_data) != "dict":
                    project_budget_data = project_budget_data.dict()
                project_budget = project_budget_table.objects.create(**project_budget_data)
                project_budget.save()
                return project_budget
            raise "Null Project Budget data was given"
        except:
            raise "Internal Server Error"
    
    def get_project_budgets(request):
        try:
            return project_budget_table.objects.filter(is_active=True).order_by("-created_on")
        except:
            raise "Internal Server Error"
        

        