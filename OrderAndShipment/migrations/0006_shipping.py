# Generated by Django 5.1.3 on 2024-12-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderAndShipment', '0005_delete_transaction_alter_rating_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('dispatchRiderFullName', models.CharField(max_length=50, null=True)),
                ('dispatchRiderPhone', models.CharField(max_length=14)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(max_length=20)),
                ('shipping_status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('In Transit', 'In Transit')], default='Pending', max_length=20)),
                ('tracking_number', models.CharField(blank=True, max_length=100, null=True)),
                ('estimated_delivery_date', models.DateField()),
            ],
        ),
    ]
