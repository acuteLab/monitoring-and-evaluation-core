# Generated by Django 4.0.5 on 2022-07-14 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_planning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsubcategory',
            name='sub_category_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project_planning.projectsubcategory', verbose_name='sub_category_of'),
        ),
    ]