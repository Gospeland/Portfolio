# Generated by Django 4.0.2 on 2022-03-21 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0011_rename_category_post_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
