# Generated by Django 2.2 on 2019-04-20 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20190415_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_order', to='profiles.Order', verbose_name='Ордер'),
        ),
    ]
