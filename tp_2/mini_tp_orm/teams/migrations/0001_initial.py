# Generated by Django 5.0.2 on 2024-06-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('color1', models.CharField(max_length=7)),
                ('color2', models.CharField(max_length=7)),
            ],
        ),
    ]
