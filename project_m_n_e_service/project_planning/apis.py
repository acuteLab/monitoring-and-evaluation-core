from ninja import Router
from config.auths import GlobalAuth
from typing import List
from .views import Project, ProjectCategory, ProjectSubCategory
from .schemas import (
    CreateProjectCategorySchema,
    CreateProjectSchema,
    CreateProjectSubCategorySchema,
    ProjectCategorySchema,
    ProjectSchema,
    ProjectSubCategorySchema,
)

# auth=GlobalAuth
project_api = Router()
category_api = Router()
sub_category_api = Router()

# Category APIs
@category_api.post("/project-category", response=ProjectCategorySchema)
def create_project_category(request, project_category: CreateProjectCategorySchema):
    return ProjectCategory.create_project_category(request, project_category)


@category_api.get("/project-categories", response=List[ProjectCategorySchema])
def get_categories(request):
    return ProjectCategory.get_project_categories(request)


@category_api.get("/project-category")
def get_category(request, categoryId: str):
    return ProjectCategory.get_project_category(request, categoryId)


@category_api.delete("/deactivate-category")
def deactivate_category(request, categoryId: str):
    return ProjectCategory.deactivate_project_category(request, categoryId)


@category_api.delete("/project-category")
def delete_category(request, categoryId: str):
    return ProjectCategory.delete_project_category(request, categoryId)


# Sub Category APIs
@sub_category_api.post("/sub-category", response=ProjectSubCategorySchema)
def create_sub_project_category(request, project_category: CreateProjectSubCategorySchema):
    return ProjectSubCategory.create_project_sub_category(request, project_category)


@sub_category_api.get("/sub-categories", response=List[ProjectSubCategorySchema])
def get_sub_categories(request):
    return ProjectSubCategory.get_project_sub_categories(request)


@sub_category_api.get("/sub-category", response=ProjectSubCategorySchema)
def get_sub_category(request, categoryId: str):
    return ProjectSubCategory.get_project_sub_category(request, categoryId)


@sub_category_api.delete("/deactivate-sub-category")
def deactivate_sub_category(request, categoryId: str):
    return ProjectSubCategory.deactivate_project_sub_category(request, categoryId)


@sub_category_api.delete("/sub-category")
def delete_sub_category(request, categoryId: str):
    return ProjectSubCategory.delete_project_sub_category(request, categoryId)


# Project APIs
@project_api.post("/project", response=ProjectSchema)
def create_project(request, project: CreateProjectSchema):
    return Project.create_project(request, project)


@project_api.get("/projects", response=List[ProjectSchema])
def get_projects(request):
    return Project.get_projects(request)


@project_api.get("/project", response=ProjectSchema)
def get_project(request, projectId: str):
    return Project.get_project(request, projectId)


@project_api.delete("/project")
def deactivate_project(request, projectId: str):
    return Project.deactivate_project(request, projectId)


@project_api.delete("/project")
def delete_project(request, projectId: str):
    return Project.delete_project(request, projectId)
