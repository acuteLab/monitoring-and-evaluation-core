from cmath import exp
from re import sub
from tempfile import TemporaryFile
from django.shortcuts import render
from .models import (
    Project as project_table,
    ProjectCategory as project_category_table,
    ProjectSubCategory as project_sub_category_table,
)
from .schemas import (
    CreateProjectCategorySchema,
    CreateProjectSubCategorySchema,
    ProjectSchema,
)


class ProjectCategory:
    def __init__(self,  *args, **kwargs):
        pass

    def create_project_category(request, project_category_data: CreateProjectCategorySchema):
        try:
            if project_category_data:
                project_category = project_category_table.objects.create(
                    **project_category_data
                )
                project_category.save()
                return project_category
            raise "Empty values was sent"
        except:
            pass

    def get_project_categories(request):
        try:
            project_categories = project_category_table.objects.filter(
                is_active=True
            ).order_by("-created_on")
            return project_categories
        except:
            pass

    def get_project_category(request,category_id: str):
        try:
            if category_id:
                project_category = project_category_table.objects.filter(
                    is_active=True, id=category_id
                )
                if project_category:
                    return project_category
                else:
                    raise "Project category not found"
            raise " null category Id was given"
        except:
            pass

    def deactivate_project_category(request, category_id: str):
        try:
            if category_id:
                updated_category = project_category_table.objects.filter(
                    id=category_id
                ).update(is_active=False)
                if updated_category:
                    return "Project Category was successful Deleted"
                return "Project Category failed to be deleted try again"
            raise "Null Project Category Id was given"
        except:
            pass

    def delete_project_category(request, category_id: str):
        try:
            if category_id:
                project_category_table.objects.filter(id=category_id).delete()
                return "Project Category Was successful Deleted "
            raise "Null Project category Id was given"

        except:
            pass


class ProjectSubCategory:
    def __init__(self,  *args, **kwargs):
        pass

    def create_project_sub_category(request, sub_category_data: CreateProjectSubCategorySchema):
        try:
            if sub_category_data:
                project_sub_category = project_sub_category_table.objects.create(
                    **sub_category_data
                )
                project_sub_category.save()
                if project_sub_category:
                    return project_sub_category
                raise "failed to save Project sub category data, please try again"
            raise "Empty Values was sent"
        except:
            pass

    def get_project_sub_categories(request):
        try:
            project_sub_categories = project_sub_category_table.objects.filter(
                is_active=True
            ).order_by("-created_on")
            return project_sub_categories
        except:
            pass

    def get_project_sub_category(request, sub_category_id: str):
        try:
            if sub_category_id:
                project_sub_category = project_sub_category_table.objects.filter(
                    is_active=True, id=sub_category_id
                )
                if project_sub_category:
                    return project_sub_category
                raise "Project Sub Category was not Found"
            raise "Null Sub Category Id was Given"
        except:
            pass
        
    def deactivate_sub_category(request, sub_category_id: str):
        try:
            if sub_category_id:
                project_sub_category_table.objects.filter(id=sub_category_id).update(is_active=False)
                return "Project sub category was Deleted (Deactivated) Successful"
            raise "Null Project sub category Id was given"
        except:
            pass
        
    def delete_sub_category(request, sub_category_id: str):
        try:
            if sub_category_id:
                project_sub_category_table.objects.filter(id=sub_category_id)
                return "Project Sub Category wa successful deleted"
            raise "Null Project Sub Category Id was Given"
        except:
            pass
            
                


class Project:
    def __init__(self, *args, **kwargs):
        pass

    def create_project(request, project_data: ProjectSchema):
        try:
            project = project_table.objects.create(**project_data)
            project.save()
            return project

        except:
            pass

    def get_projects(request):
        try:
            projects = project_table.objects.filter(is_active=True)
            return projects
        except:
            pass
        
        
    def get_project(request, project_id: str):
        try:
            if project_id:
                project = project_table.objects.filter(is_active=True, id=project_id)
                return project
            raise "Null Project Id was given"
        except:
            pass
        
    def deactivate_project(request, project_id: str):
        try:
            if project_id:
                project_table.objects.filter(id=project_id).update(is_active=False)
                return "Project was deleted (Deactivated) Successfuly"
            raise "Null Project Id was Given"
        except:
            pass
        
    def delete_project(request, project_id: str):
        try:
            if project_id:
                project_table.objects.filter(id=project_id).delete()
                return "Project was Successful Deleted"
            raise "NUll Project Id was given"
        except:
            pass
