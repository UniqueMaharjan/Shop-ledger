# Generated by Django 3.2.5 on 2021-09-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopledgerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
