# Generated by Django 3.0 on 2022-02-18 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login_Delivery',
            new_name='Order',
        ),
    ]
