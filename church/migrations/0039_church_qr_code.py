# Generated by Django 5.2 on 2025-07-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0038_alter_memberchatmessage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='church',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='church_qrcodes/'),
        ),
    ]
