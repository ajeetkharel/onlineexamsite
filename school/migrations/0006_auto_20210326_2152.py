# Generated by Django 3.1.3 on 2021-03-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.IntegerField(default=0),
        ),
    ]
