# Generated by Django 2.1.7 on 2019-04-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angel', '0005_angel_im_token'),
        ('info', '0002_auto_20190404_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='angels',
        ),
        migrations.AddField(
            model_name='info',
            name='angel',
            field=models.ManyToManyField(blank=True, null=True, to='angel.Angel'),
        ),
    ]