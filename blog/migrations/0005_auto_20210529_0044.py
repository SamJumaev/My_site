# Generated by Django 3.2.3 on 2021-05-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210528_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='pictures')),
                ('name', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.DeleteModel(
            name='AboutMe',
        ),
        migrations.RemoveField(
            model_name='aboutmyskills',
            name='skills',
        ),
        migrations.DeleteModel(
            name='Myself',
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
        migrations.AddField(
            model_name='skills',
            name='class_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='AboutMySkills',
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.ManyToManyField(to='blog.Skills'),
        ),
    ]