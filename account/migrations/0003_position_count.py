# Generated by Django 2.1.7 on 2019-02-19 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190220_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
