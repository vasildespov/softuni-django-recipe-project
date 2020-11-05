# Generated by Django 3.1.2 on 2020-11-03 23:57

from django.db import migrations, models
import project_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0003_auto_20201103_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(max_length=250, verbose_name="Ingredients (Please separate the ingredients with ','"),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(validators=[project_app.validators.time_validator], verbose_name='Time (Minutes)'),
        ),
    ]
