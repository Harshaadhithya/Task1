# Generated by Django 4.2.3 on 2023-07-25 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_importedcontact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importedcontact',
            name='organization',
        ),
    ]