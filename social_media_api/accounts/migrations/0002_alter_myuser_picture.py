# Generated by Django 5.0.2 on 2024-12-27 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='picture',
            field=models.ImageField(upload_to='accounts/y/m/%d'),
        ),
    ]