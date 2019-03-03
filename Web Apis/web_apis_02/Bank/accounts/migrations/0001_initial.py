# Generated by Django 2.1.5 on 2019-03-02 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('balance', models.FloatField(default=0.0)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
