# Generated by Django 2.1.5 on 2020-09-09 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='Mamamaa', max_length=120),
        ),
    ]