# Generated by Django 4.1.5 on 2023-02-20 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_alter_employee_snils_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['personnel_number', 'surname', 'firstname', 'other_name']},
        ),
    ]