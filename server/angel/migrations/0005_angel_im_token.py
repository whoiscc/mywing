# Generated by Django 2.1.7 on 2019-03-31 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angel', '0004_auto_20190212_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='angel',
            name='im_token',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
