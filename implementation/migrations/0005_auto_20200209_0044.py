# Generated by Django 3.0.2 on 2020-02-08 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('implementation', '0004_auto_20200120_1237'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImplementationModel',
            new_name='Nums',
        ),
        migrations.AlterModelTable(
            name='nums',
            table='nums',
        ),
    ]