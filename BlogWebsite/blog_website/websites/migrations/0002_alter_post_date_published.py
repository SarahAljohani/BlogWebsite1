# Generated by Django 5.0.7 on 2024-07-11 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(),
        ),
    ]
