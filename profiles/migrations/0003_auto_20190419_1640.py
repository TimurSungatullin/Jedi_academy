# Generated by Django 2.2 on 2019-04-19 13:40

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20190415_1810'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='jedi',
            managers=[
                ('count', django.db.models.manager.Manager()),
            ],
        ),
    ]