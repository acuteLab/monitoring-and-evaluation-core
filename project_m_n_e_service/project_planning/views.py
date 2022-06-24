from cmath import exp
from re import sub
from tempfile import TemporaryFile
from django.shortcuts import render
from .models import (
    Project as project_table,
    ProjectCategory as project_category_table,
    ProjectSubCategory as project_sub_category_table,
)


class ProjectCategory:
    def __init__(self, *args, **kwargs):
        pass

    def create_project_category(request, project_category_data):
        try:
            if project_category_data:
                if type(project_category_data) != "dict":
                    project_category_data = project_category_data.dict()
                project_category = project_category_table.objects.create(
                    **project_category_data
                ).save()
                return project_category
            raise "Empty values was sent"
        except:
            raise "Internal Server Error"

    def update_project_category(request, category_id, category_data):
        try:
            if category_id:
                category = project_category_table.filter(id=category_id)
                if category:
                    if category_data:
                        category.update(**category_data)
                        return category
                    raise "Null Data was given"
                raise "Category was not found"
            raise "Null Category Id was given"
        except:
           raise "Internal Server Error"

    def get_project_categories(request):
        try:
            project_categories = project_category_table.objects.filter(
                is_active=True
            ).order_by("-created_on")
            return project_categories
        except:
           raise "Internal Server Error"

    def get_project_category(request, category_id: str):
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
            raise "Internal Server Error"

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
            raise "Internal Server Error"


class ProjectSubCategory:
    def __init__(self, *args, **kwargs):
        pass

    def create_project_sub_category(request, sub_category_data):
        try:
            if sub_category_data:
                if type(sub_category_data) != "dict":
                    sub_category_data = sub_category_data.dict()
                project_sub_category = project_sub_category_table.objects.create(
                    **sub_category_data
                )
                project_sub_category.save()
                if project_sub_category:
                    return project_sub_category
                raise "failed to save Project sub category data, please try again"
            raise "Empty Values was sent"
        except:
            raise "Internal Server Error"

    def get_project_sub_categories(request):
        try:
            project_sub_categories = project_sub_category_table.objects.filter(
                is_active=True
            ).order_by("-created_on")
            return project_sub_categories
        except:
            raise "Internal Server Error"

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
            raise "Internal Server Error"

    def deactivate_sub_category(request, sub_category_id: str):
        try:
            if sub_category_id:
                project_sub_category_table.objects.filter(id=sub_category_id).update(
                    is_active=False
                )
                return "Project sub category was Deleted (Deactivated) Successful"
            raise "Null Project sub category Id was given"
        except:
            raise "Internal Server Error"

    def delete_sub_category(request, sub_category_id: str):
        try:
            if sub_category_id:
                project_sub_category_table.objects.filter(id=sub_category_id)
                return "Project Sub Category wa successful deleted"
            raise "Null Project Sub Category Id was Given"
        except:
            raise "Internal Server Error"


class Project:
    def __init__(self, *args, **kwargs):
        pass

    def create_project(request, project_data):
        try:
            project = project_table.objects.create(**project_data)
            project.save()
            return project

        except:
            raise "Internal Server Error"

    def get_projects(request):
        try:
            projects = project_table.objects.filter(is_active=True).order_by(
                "-created_on"
            )
            return projects
        except:
            raise "Internal Server Error"

    def get_project(request, project_id: str):
        try:
            if project_id:
                project = project_table.objects.filter(is_active=True, id=project_id)
                return project
            raise "Null Project Id was given"
        except:
            raise "Internal Server Error"

    def deactivate_project(request, project_id: str):
        try:
            if project_id:
                project_table.objects.filter(id=project_id).update(is_active=False)
                return "Project was deleted (Deactivated) Successfuly"
            raise "Null Project Id was Given"
        except:
            raise "Internal Server Error"

    def delete_project(request, project_id: str):
        try:
            if project_id:
                project_table.objects.filter(id=project_id).delete()
                return "Project was Successful Deleted"
            raise "NUll Project Id was given"
        except:
            raise "Internal Server Error"
