# Generated by Django 4.1.3 on 2022-12-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enzi_app', '0002_rename_checkin_date_clientbooking_checkin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]
