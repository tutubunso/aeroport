# Generated by Django 3.0.7 on 2020-07-09 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vols',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('villedepart', models.CharField(max_length=25)),
                ('villearrivee', models.CharField(max_length=30)),
            ],
        ),
    ]