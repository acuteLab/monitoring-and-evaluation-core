# Generated by Django 4.0.5 on 2022-07-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_planning', '0002_alter_projectsubcategory_sub_category_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='country',
            field=models.CharField(max_length=3),
        ),
    ]
