# Generated by Django 5.1.3 on 2024-12-14 13:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('billing_firstName', models.CharField(max_length=30)),
                ('billing_secondName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('billing_country', models.CharField(max_length=20)),
                ('billing_state', models.CharField(max_length=20)),
                ('billing_homeaddress', models.CharField(max_length=50)),
                ('billing_postalcode', models.CharField(max_length=6)),
                ('billing_ordernote', models.CharField(blank=True, max_length=255, null=True)),
                ('delivery_firstName', models.CharField(max_length=30)),
                ('delivery_secondName', models.CharField(max_length=30)),
                ('delivery_email', models.EmailField(max_length=254)),
                ('delivery_phoneNumber', models.CharField(max_length=13)),
                ('delivery_country', models.CharField(max_length=20)),
                ('delivery_state', models.CharField(max_length=50)),
                ('delivery_homeaddress', models.CharField(max_length=50)),
                ('delivery_postalcode', models.CharField(max_length=6)),
                ('shippingMethod', models.CharField(choices=[('Air Courier', 'Air Courier'), ('Land Courier', 'Land Courier')], max_length=20)),
                ('duties', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('paymentMethod', models.CharField(choices=[('paystack', 'paystack'), ('Bank Transfer', 'Bank Transfer')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=60)),
                ('active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
