# Generated by Django 4.2.13 on 2024-06-01 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_alter_question_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
