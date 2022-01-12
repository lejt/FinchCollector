# Generated by Django 4.0.1 on 2022-01-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('family', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=150)),
                ('fav_food', models.CharField(max_length=20)),
                ('weight', models.IntegerField()),
            ],
        ),
    ]