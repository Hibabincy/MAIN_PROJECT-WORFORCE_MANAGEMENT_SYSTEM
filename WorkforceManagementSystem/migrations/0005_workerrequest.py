# Generated by Django 4.0.1 on 2024-03-06 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WorkforceManagementSystem', '0004_jobrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workerrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('EMPLOYER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkforceManagementSystem.employer')),
                ('WORKER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkforceManagementSystem.worker')),
            ],
        ),
    ]
