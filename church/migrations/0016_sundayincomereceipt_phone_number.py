# Generated by Django 5.2 on 2025-06-20 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0015_onlinegiving_receipt_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='sundayincomereceipt',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
