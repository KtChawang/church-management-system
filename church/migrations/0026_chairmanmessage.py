# Generated by Django 5.2 on 2025-07-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0025_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChairmanMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default="Message from the Chairman's Desk", max_length=200)),
                ('message', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='chairman/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
