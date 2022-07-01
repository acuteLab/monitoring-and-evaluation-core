from ninja.orm import create_schema
from .models import ProjectBudget, ProjectDeliverableBudget
from config.base_model import excluding_parameters


ProjectBudgetSchema = create_schema(ProjectBudget)
CreateProjectBudgetSchema = create_schema(ProjectBudget, exclude=excluding_parameters)

ProjectDeliverableBudgetSchema = create_schema(ProjectDeliverableBudget)
CreateProjectDeliverableBudgetSchema = create_schema(ProjectDeliverableBudget, exclude=excluding_parameters)
