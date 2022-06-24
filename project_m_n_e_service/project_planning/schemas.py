from ninja.orm import create_schema
import uuid
from typing import List
from .models import (
    Project,
    ProjectCategory,
    ProjectDeliverable,
    ProjectSubCategory,
)

excluding_parameters = ["id", "created_on", "updated_on", "is_active", "created_by"]


ProjectCategorySchema = create_schema(ProjectCategory)
CreateProjectCategorySchema = create_schema(
    ProjectCategory, exclude=excluding_parameters
)

ProjectSubCategorySchema = create_schema(ProjectSubCategory)
CreateProjectSubCategorySchema = create_schema(
    ProjectSubCategory, exclude=excluding_parameters
)

ProjectSchema = create_schema(Project)
CreateProjectSchema = create_schema(Project, exclude=excluding_parameters)

ProjectDeliverableSchema = create_schema(ProjectDeliverable)
CreateProjectDeliverableSchema = create_schema(
    ProjectDeliverable, exclude=excluding_parameters
)
