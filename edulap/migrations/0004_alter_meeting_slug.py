# Generated by Django 4.2.5 on 2023-10-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edulap', '0003_rename_metting_meeting_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
