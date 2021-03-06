# Generated by Django 2.2 on 2019-04-30 19:26

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0059_auto_20190422_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ocpawscostlineitemprojectdailysummary',
            old_name='project_cost',
            new_name='pod_cost',
        ),
        migrations.RemoveField(
            model_name='ocpawscostlineitemprojectdailysummary',
            name='shared_projects',
        ),
        migrations.AddField(
            model_name='ocpawscostlineitemprojectdailysummary',
            name='pod',
            field=models.CharField(max_length=253, null=True),
        ),
        migrations.AddField(
            model_name='ocpawscostlineitemprojectdailysummary',
            name='pod_labels',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.RemoveIndex(
            model_name='ocpawscostlineitemprojectdailysummary',
            name='cost_proj_tags_idx',
        ),
        migrations.RemoveField(
            model_name='ocpawscostlineitemprojectdailysummary',
            name='tags',
        ),
        migrations.AddIndex(
            model_name='ocpawscostlineitemprojectdailysummary',
            index=django.contrib.postgres.indexes.GinIndex(fields=['pod_labels'], name='cost_proj_pod_labels_idx'),
        ),
    ]
