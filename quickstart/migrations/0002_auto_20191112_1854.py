# Generated by Django 2.0.7 on 2019-11-12 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Board',
        ),
    ]