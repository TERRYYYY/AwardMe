# Generated by Django 3.0.7 on 2020-06-06 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=255)),
                ('project_pic', models.ImageField(default='title', upload_to='projects/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.FloatField()),
                ('usability', models.FloatField()),
                ('content', models.FloatField()),
                ('average', models.FloatField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.Project')),
            ],
            options={
                'ordering': ['average'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default=' ', upload_to='profiles/')),
                ('bio', models.TextField()),
                ('contact', models.CharField(max_length=255, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.Project')),
            ],
            options={
                'ordering': ['contact'],
            },
        ),
    ]
