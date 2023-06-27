# Generated by Django 4.2.1 on 2023-06-22 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("engine", "0070_add_job_type_created_date"),
        ("quality_control", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="qualityreport",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quality_reports",
                to="engine.project",
            ),
        ),
        migrations.AddField(
            model_name="qualitysettings",
            name="project",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quality_settings",
                to="engine.project",
            ),
        ),
        migrations.AlterField(
            model_name="qualityreport",
            name="gt_last_updated",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="qualitysettings",
            name="task",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quality_settings",
                to="engine.task",
            ),
        ),
    ]