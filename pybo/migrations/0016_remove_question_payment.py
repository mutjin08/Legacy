# Generated by Django 3.2.19 on 2023-05-19 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0015_alter_question_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='payment',
        ),
    ]
