# Generated by Django 5.0.6 on 2024-05-16 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_studentfeebalance_term'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentfeebalance',
            old_name='amount',
            new_name='balance',
        ),
    ]