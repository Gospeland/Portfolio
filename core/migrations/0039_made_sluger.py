# Generated by Django 4.0.2 on 2022-04-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_rename_imager_made'),
    ]

    operations = [
        migrations.AddField(
            model_name='made',
            name='sluger',
            field=models.SlugField(null=True),
        ),
    ]