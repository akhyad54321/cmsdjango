# Generated by Django 4.0.3 on 2022-03-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_rename_compnay_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(default=' ', max_length=13),
        ),
    ]