# Generated by Django 2.2.1 on 2019-05-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0003_auto_20190528_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='GoodHotSale',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
