# Generated by Django 4.2.3 on 2024-02-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_admin_registration_manager_registration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_type', models.CharField(max_length=20)),
                ('Room_Number', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Room_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Members', models.CharField(max_length=10)),
                ('room_allotted', models.ManyToManyField(to='app.rooms')),
            ],
        ),
    ]