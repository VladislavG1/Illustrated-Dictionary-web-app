# Generated by Django 4.2.10 on 2024-05-16 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cyrillic'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'word_day',
                'managed': False,
            },
        ),
    ]
