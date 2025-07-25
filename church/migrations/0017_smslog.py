# Generated by Django 5.2 on 2025-06-20 09:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0016_sundayincomereceipt_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('success', models.BooleanField(default=False)),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.church')),
            ],
        ),
    ]
