# Generated by Django 2.0.2 on 2018-02-05 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180205_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
