# Generated by Django 2.0.7 on 2018-11-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='article',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
