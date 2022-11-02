# Generated by Django 4.1 on 2022-11-01 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Applicant'), (2, 'Employer')], default=1),
        ),
    ]
