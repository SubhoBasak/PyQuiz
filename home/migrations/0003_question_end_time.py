# Generated by Django 3.1.2 on 2020-10-13 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
    ]