# Generated by Django 3.0.7 on 2020-10-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutu', '0005_paiement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='image/picture'),
        ),
    ]
