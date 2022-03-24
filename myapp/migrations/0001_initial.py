# Generated by Django 4.0.2 on 2022-03-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=40)),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]