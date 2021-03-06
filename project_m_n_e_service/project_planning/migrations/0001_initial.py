# Generated by Django 4.0.5 on 2022-07-01 15:53

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=4000, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=8000, null=True)),
                ('description', models.TextField(blank=True, max_length=100000, null=True)),
                ('estimate_time_line', models.IntegerField(blank=True, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=4000, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=4000)),
                ('short_name', models.CharField(blank=True, max_length=4000, null=True)),
            ],
            options={
                'db_table': 'project_category',
            },
        ),
        migrations.CreateModel(
            name='ProjectSubCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=4000, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=300)),
                ('short_name', models.CharField(blank=True, max_length=300, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project_planning.projectcategory')),
                ('sub_category_of', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project_planning.projectsubcategory', verbose_name='sub_category_of')),
            ],
            options={
                'verbose_name': 'ProjectSubCategory',
                'verbose_name_plural': 'ProjectSubCategorys',
                'db_table': 'project_sub_category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProjectDeliverable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=4000, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deliverable', models.CharField(blank=True, max_length=400, null=True)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('planned_start_date', models.DateTimeField(blank=True, null=True)),
                ('actual_start_date', models.DateTimeField(blank=True, null=True)),
                ('planned_end_date', models.DateTimeField(blank=True, null=True)),
                ('actual_end_date', models.DateTimeField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project_planning.project')),
            ],
            options={
                'verbose_name': 'Project Deliverable',
                'verbose_name_plural': 'Project Deliverables',
                'db_table': 'project_deliverable',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='project',
            name='project_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project_planning.projectsubcategory'),
        ),
    ]
