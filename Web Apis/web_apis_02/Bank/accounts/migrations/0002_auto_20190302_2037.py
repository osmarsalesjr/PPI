# Generated by Django 2.1.5 on 2019-03-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.FloatField(),
        ),
    ]
