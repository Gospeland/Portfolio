# Generated by Django 4.0.2 on 2022-03-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_authorprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorprofile',
            name='occupation',
            field=models.CharField(max_length=200, null=True),
        ),
    ]