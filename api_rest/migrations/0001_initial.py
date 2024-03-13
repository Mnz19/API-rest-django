# Generated by Django 5.0.3 on 2024-03-13 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(default='', max_length=100)),
                ('user_email', models.EmailField(default='', max_length=100)),
                ('user_age', models.CharField(default='', max_length=100)),
            ],
        ),
    ]