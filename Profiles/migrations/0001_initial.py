# Generated by Django 4.1.3 on 2022-11-16 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('web_page_link', models.URLField()),
                ('photo', models.URLField()),
            ],
        ),
    ]
