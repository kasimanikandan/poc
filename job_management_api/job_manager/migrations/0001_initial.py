# Generated by Django 3.2.6 on 2021-10-18 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=250)),
                ('skills', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('created_on', models.DateTimeField()),
            ],
        ),
    ]