# Generated by Django 4.1.7 on 2023-03-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
