# Generated by Django 4.0 on 2021-12-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datastore', '0002_alter_dataset_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='path',
            field=models.FilePathField(path='./dataset/'),
        ),
    ]
