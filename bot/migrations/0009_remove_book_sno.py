# Generated by Django 4.2.5 on 2023-10-13 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_rename_sno_book_sno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Sno',
        ),
    ]
