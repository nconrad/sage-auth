# Generated by Django 3.0.4 on 2020-03-10 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='scope',
            field=models.TextField(default='default'),
        ),
    ]