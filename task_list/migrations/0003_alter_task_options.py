# Generated by Django 4.1.1 on 2022-09-25 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_list', '0002_rename_tasks_task_tags_alter_task_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status', '-datetime']},
        ),
    ]
