# Generated by Django 2.2.4 on 2019-08-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuildingPlat', '0004_auto_20190823_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winbid',
            name='crawltime',
            field=models.DateTimeField(null=True, verbose_name='爬取时间'),
        ),
    ]