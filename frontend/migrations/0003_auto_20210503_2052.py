# Generated by Django 3.2 on 2021-05-04 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20210503_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gyke',
            name='artiste6',
        ),
        migrations.RemoveField(
            model_name='gyke',
            name='pst_music6',
        ),
        migrations.RemoveField(
            model_name='gyke',
            name='song6',
        ),
    ]
