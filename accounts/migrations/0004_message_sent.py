# Generated by Django 4.1.4 on 2023-01-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
