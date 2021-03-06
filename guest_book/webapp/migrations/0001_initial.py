# Generated by Django 3.1.6 on 2021-03-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('text', models.TextField(max_length=300)),
                ('cread_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=100)),
            ],
        ),
    ]
