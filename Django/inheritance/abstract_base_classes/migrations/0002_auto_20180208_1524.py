# Generated by Django 2.0.2 on 2018-02-08 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstract_base_classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='home_group',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
