from typing import List
from ninja import Router
from config.auths import GlobalAuth
from .views import ProjectBudget, Currency
from .schemas import CreateProjectBudgetSchema, ProjectBudgetSchema

auth=GlobalAuth()
project_budget_api = Router()



@project_budget_api.post("/project-budget", response=ProjectBudgetSchema)
def create_project_budget(request, project_budget: CreateProjectBudgetSchema):
    return ProjectBudget.create_project_budget(request, project_budget)


@project_budget_api.get("/project-budgets", response=List[ProjectBudgetSchema])
def get_categories(request):
    return ProjectBudget.get_project_budgets(request)