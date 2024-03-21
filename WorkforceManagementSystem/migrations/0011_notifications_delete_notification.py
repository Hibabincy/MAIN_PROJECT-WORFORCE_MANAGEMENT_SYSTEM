# Generated by Django 4.0.1 on 2024-03-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkforceManagementSystem', '0010_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notification_name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=300)),
                ('Date', models.DateField()),
                ('Status', models.CharField(default='', max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
