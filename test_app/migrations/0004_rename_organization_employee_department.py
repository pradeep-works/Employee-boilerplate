# Generated by Django 5.0.3 on 2024-03-26 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_department_employee_designation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='organization',
            new_name='department',
        ),
    ]
