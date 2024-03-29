# Generated by Django 2.2.6 on 2019-10-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=98)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
