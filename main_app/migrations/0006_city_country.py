# Generated by Django 3.1.2 on 2020-10-09 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20201009_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]