# Generated by Django 3.2.5 on 2021-07-09 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]