# Generated by Django 4.2.5 on 2023-10-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('PayPal', 'PayPal')], max_length=100),
        ),
    ]