# Generated by Django 4.2.5 on 2023-10-21 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_tax'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tax',
            options={'verbose_name_plural': 'Tax'},
        ),
    ]