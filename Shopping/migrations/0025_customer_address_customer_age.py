# Generated by Django 4.0.3 on 2022-04-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0024_customer_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]