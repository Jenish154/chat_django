# Generated by Django 4.1.4 on 2023-01-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
