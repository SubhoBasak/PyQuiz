# Generated by Django 3.1.2 on 2020-10-15 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_question_confidence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='confidence',
        ),
        migrations.AddField(
            model_name='questionset',
            name='confidence',
            field=models.FloatField(default=0.0, verbose_name='Confidence'),
        ),
    ]
