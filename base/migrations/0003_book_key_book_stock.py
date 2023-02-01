# Generated by Django 4.1.5 on 2023-02-01 16:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_book_key_remove_book_stock_alter_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='key',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]