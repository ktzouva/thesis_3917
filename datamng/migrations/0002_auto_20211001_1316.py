# Generated by Django 3.1 on 2021-10-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showndata',
            name='data',
            field=models.CharField(max_length=1000000000000),
        ),
    ]
