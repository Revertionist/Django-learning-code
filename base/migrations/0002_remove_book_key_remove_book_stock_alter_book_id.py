# Generated by Django 4.1.5 on 2023-02-01 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='key',
        ),
        migrations.RemoveField(
            model_name='book',
            name='stock',
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
