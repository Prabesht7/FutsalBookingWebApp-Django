# Generated by Django 4.0.3 on 2022-04-12 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0021_alter_customer_avatar'),
        ('Booking', '0006_booking_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to='Shopping.customer'),
        ),
    ]
