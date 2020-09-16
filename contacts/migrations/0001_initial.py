# Generated by Django 3.1.1 on 2020-09-16 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('info', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date', models.DateField(auto_now_add=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
