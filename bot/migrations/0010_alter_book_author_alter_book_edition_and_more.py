# Generated by Django 4.2.5 on 2023-10-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_remove_book_sno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Author',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='Edition',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='PublishedBy',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='RefVol',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='TotalVol',
            field=models.IntegerField(null=True),
        ),
    ]
