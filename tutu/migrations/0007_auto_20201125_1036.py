# Generated by Django 3.0.7 on 2020-11-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutu', '0006_auto_20201027_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='media/image/picture'),
        ),
    ]