from ninja import Router
from config.auths import GlobalAuth
from typing import List
from .views import Project, ProjectCategory
from .schemas import CreateProjectCategorySchema, CreateProjectSchema, ProjectCategorySchema, ProjectSchema
# auth=GlobalAuth
project_api = Router()
category_api = Router()
sub_category_api = Router()

@category_api.post("/project-category", response=ProjectCategorySchema)
def create_project_category(request, project_category: CreateProjectCategorySchema):
    return ProjectCategory.create_project_category(request, project_category)


@category_api.get("/project-categories")
def get_categories(request):
    return ProjectCategory.get_project_categories(request)

@category_api.get("/project-category")
def get_category(request, category_id: str):
    return ProjectCategory.get_project_category(request, category_id)

@project_api.post("/project", response=ProjectSchema)
def create_project(request, project: CreateProjectSchema):
    return Project.create_project(request, project)

@project_api.get("/projects")
def get_projects(request):
    return Project.get_projects(request)

@project_api.get("/project")
def get_project(request, id: str):
    return Project.get_project(request, id)


@project_api.delete("/project")
def deactivate_project(request, id: str):
    return Project.deactivate_project(request, id)


@project_api.delete("/project")
def delete_project(request, id: str):
    return Project.delete_project(request, id)
