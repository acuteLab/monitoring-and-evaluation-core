from urllib import response
from ninja import Router
from config.auths import GlobalAuth
from typing import List
from .views import Project, ProjectCategory, ProjectSubCategory, ProjectDeliverable
from .schemas import (
    CreateProjectCategorySchema,
    CreateProjectDeliverableSchema,
    CreateProjectSchema,
    CreateProjectSubCategorySchema,
    ProjectCategorySchema,
    ProjectDeliverableSchema,
    ProjectSchema,
    ProjectSubCategorySchema,
)

auth=GlobalAuth()
category_api = Router(auth=auth)
sub_category_api = Router(auth=auth)
project_api = Router(auth=auth)
project_deliverable_api = Router(auth=auth)

# Category APIs
@category_api.post("/project-category", response=ProjectCategorySchema)
def create_project_category(request, project_category: CreateProjectCategorySchema):
    return ProjectCategory.create_project_category(request, project_category)


@category_api.get("/project-categories", response=List[ProjectCategorySchema])
def get_categories(request):
    return ProjectCategory.get_project_categories(request)


@category_api.get("/project-category", response=ProjectCategorySchema)
def get_category(request, categoryId: str):
    return ProjectCategory.get_project_category(request, categoryId)

@category_api.patch("/project-category", response=ProjectCategorySchema)
def update_category(request, categoryId: str, projectCategory: CreateProjectCategorySchema):
    return ProjectCategory.update_project_category(request, categoryId, projectCategory)


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
def get_sub_category(request, subCategoryId: str):
    return ProjectSubCategory.get_project_sub_category(request, subCategoryId)

@sub_category_api.get("/category/sub-categories", response=List[ProjectSubCategorySchema])
def get_sub_category_by_category_id(request, categoryId: str):
    return ProjectSubCategory.get_sub_category_by_category(request, categoryId)

@sub_category_api.patch("/sub-category", response=ProjectSubCategorySchema)
def update_sub_category(request, subCategoryId: str, subCategory: CreateProjectSubCategorySchema):
    return ProjectSubCategory.update_project_sub_category(request, subCategoryId, subCategory)


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

@project_api.get("/category/projects", response=List[ProjectSchema])
def get_project_by_category_id(request, categoryId: str):
    return Project.get_project_by_category(request, categoryId)


@project_api.patch("/project", response=ProjectSchema)
def deactivate_project(request, projectId: str, project: CreateProjectSchema):
    return Project.update_project(request, projectId, project)

@project_api.delete("/project")
def deactivate_project(request, projectId: str):
    return Project.deactivate_project(request, projectId)


@project_api.delete("/project")
def delete_project(request, projectId: str):
    return Project.delete_project(request, projectId)


# Project Deliverables APIs
@project_deliverable_api.post("/project-deliverable", response= ProjectDeliverableSchema)
def create_project_deliverable(request, projectDeliverable: CreateProjectDeliverableSchema):
    return ProjectDeliverable.create_project_deliverable(request, projectDeliverable)


@project_deliverable_api.get("/project-deliverables", response=List[ProjectDeliverableSchema])
def get_project_deliverables(request):
    return ProjectDeliverable.get_project_deliverables(request)


@project_deliverable_api.get("/project-deliverable", response=ProjectDeliverableSchema)
def get_project_deliverable(request, deliverableId: str):
    return ProjectDeliverable.get_project_deliverable(request, deliverableId)

@project_deliverable_api.get("/project/project-deliverables", response=List[ProjectDeliverableSchema])
def get_project_deliverable_by_project_id(request, projectId: str):
    return ProjectDeliverable.get_deliverable_by_project(request, projectId)

@project_deliverable_api.patch("/project-deliverable", response=ProjectDeliverableSchema)
def update_project_deliverable(request, deliverableId: str, projectDeliverable: CreateProjectDeliverableSchema):
    return ProjectDeliverable.update_project_deliverable(request, deliverableId, projectDeliverable)

@project_deliverable_api.delete("/project-deliverable")
def deactivate_project_deliverable(request, deliverableId: str):
    return ProjectDeliverable.deactivate_project_deliverable(request, deliverableId)


@project_deliverable_api.delete("/project-deliverable")
def delete_project_deliverable(request, deliverableId: str):
    return ProjectDeliverable.delete_project_deliverable(request, deliverableId)

