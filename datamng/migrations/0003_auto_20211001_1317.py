# Generated by Django 3.1 on 2021-10-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamng', '0002_auto_20211001_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showndata',
            name='data_test',
            field=models.CharField(max_length=1000000000000),
        ),
        migrations.AlterField(
            model_name='showndata',
            name='data_train',
            field=models.CharField(max_length=1000000000000),
        ),
        migrations.AlterField(
            model_name='showndata',
            name='prediction',
            field=models.CharField(max_length=1000000000000),
        ),
        migrations.AlterField(
            model_name='showndata',
            name='target_test',
            field=models.CharField(max_length=1000000000000),
        ),
        migrations.AlterField(
            model_name='showndata',
            name='target_train',
            field=models.CharField(max_length=1000000000000),
        ),
    ]
