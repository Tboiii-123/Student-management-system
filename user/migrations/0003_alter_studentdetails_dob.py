# Generated by Django 4.1.7 on 2024-05-25 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_studentdetails_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='DOB',
            field=models.CharField(max_length=30),
        ),
    ]
