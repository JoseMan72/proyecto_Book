# Generated by Django 4.2.7 on 2023-11-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='sinopsis',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
