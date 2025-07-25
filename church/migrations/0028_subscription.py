# Generated by Django 5.2 on 2025-07-14 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0027_licensekey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('last_paid_at', models.DateField()),
                ('next_due_date', models.DateField()),
                ('plan', models.CharField(choices=[('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('church', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='church.church')),
            ],
        ),
    ]
