# Generated by Django 4.1 on 2022-11-01 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0005_alter_job_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='contact_info',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
