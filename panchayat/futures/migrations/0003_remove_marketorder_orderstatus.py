# Generated by Django 2.2.5 on 2019-12-04 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futures', '0002_marketorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketorder',
            name='OrderStatus',
        ),
    ]