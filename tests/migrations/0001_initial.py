# Generated by Django 2.2 on 2019-04-15 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='Вопрос')),
                ('correct_answer', models.BooleanField(verbose_name='Правильный ответ')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='test_order', to='profiles.Order', verbose_name='Ордер')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='test_planet', to='profiles.Planet', verbose_name='Планета')),
                ('questions', models.ManyToManyField(related_name='test_questions', to='tests.Question', verbose_name='Вопросы')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
    ]
