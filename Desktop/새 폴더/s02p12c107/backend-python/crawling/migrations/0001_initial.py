# Generated by Django 3.0.2 on 2020-01-21 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crawling',
            fields=[
                ('pcode', models.AutoField(primary_key=True, serialize=False)),
                ('pplace', models.CharField(max_length=50)),
                ('purl', models.TextField()),
                ('pname', models.CharField(max_length=50)),
                ('psource', models.CharField(max_length=25)),
            ],
        ),
    ]
