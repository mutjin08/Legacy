# Generated by Django 2.2.4 on 2023-05-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_auto_20230514_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
