# Generated by Django 2.2.4 on 2023-05-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_auto_20230514_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='output',
            field=models.FileField(blank=True, null=True, upload_to='output/'),
        ),
    ]
