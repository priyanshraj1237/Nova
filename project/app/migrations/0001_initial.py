# Generated by Django 5.1.3 on 2024-11-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=100)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(default='Not Provided', max_length=15)),
                ('age', models.CharField(default='18', max_length=3)),
                ('experience', models.CharField(default='0', help_text='Experience in years', max_length=50)),
                ('bio', models.TextField(blank=True, default='This user has not provided a bio.')),
            ],
        ),
    ]