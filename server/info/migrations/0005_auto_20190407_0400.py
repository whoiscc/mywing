# Generated by Django 2.1.7 on 2019-04-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20190407_0317'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('author', models.CharField(blank=True, max_length=64, null=True)),
                ('updatedAt', models.DateTimeField(blank=True, editable=False, null=True)),
                ('content', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='board',
            old_name='updateAt',
            new_name='updatedAt',
        ),
        migrations.RemoveField(
            model_name='board',
            name='author',
        ),
        migrations.RemoveField(
            model_name='board',
            name='content',
        ),
        migrations.RemoveField(
            model_name='board',
            name='title',
        ),
    ]
