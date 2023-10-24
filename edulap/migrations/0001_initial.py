# Generated by Django 4.2.5 on 2023-10-03 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('teacher', 'teacher'), ('student', 'student')], max_length=50)),
                ('userMail', models.EmailField(max_length=254, unique=True)),
                ('userPhone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Metting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mettingName', models.CharField(max_length=50)),
                ('mettingPrice', models.IntegerField()),
                ('slug', models.SlugField(blank=True)),
                ('customer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='edulap.customer')),
            ],
        ),
    ]
