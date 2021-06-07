# Generated by Django 3.2.3 on 2021-05-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210528_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMySkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'AboutMySkills',
                'verbose_name_plural': 'AboutMySkills',
            },
        ),
    ]
