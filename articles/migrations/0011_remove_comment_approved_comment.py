# Generated by Django 2.0.7 on 2018-11-21 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]
