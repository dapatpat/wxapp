# Generated by Django 2.2.1 on 2019-05-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestreceaddress',
            name='GReceCityID',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='guestreceaddress',
            name='GReceCityName',
            field=models.CharField(max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='guestreceaddress',
            name='GReceDistrictID',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='guestreceaddress',
            name='GReceDistrictName',
            field=models.CharField(max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='guestreceaddress',
            name='GReceProvinceID',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='guestreceaddress',
            name='GReceProvinceName',
            field=models.CharField(max_length=220, null=True),
        ),
    ]
