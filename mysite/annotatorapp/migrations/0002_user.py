# Generated by Django 2.0.4 on 2018-06-10 09:50
#generated upon applying migrations
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotatorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('savedSentence', models.CharField(max_length=100)),
                ('clickSequence', models.CharField(max_length=100)),
                ('init_time', models.TimeField(auto_now_add=True)),
                ('end_time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
