# Generated by Django 3.0.7 on 2020-06-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_res_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
