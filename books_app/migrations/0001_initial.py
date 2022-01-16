# Generated by Django 3.1.7 on 2022-01-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(blank=True, max_length=100)),
                ('publishedDate', models.CharField(blank=True, max_length=20)),
                ('ISBN', models.CharField(blank=True, max_length=20)),
                ('pageCount', models.IntegerField(blank=True, null=True)),
                ('thumbnail', models.URLField(blank=True)),
                ('language', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
