# Generated by Django 3.1.2 on 2020-11-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(verbose_name='Time (Minutes)'),
        ),
    ]