# Generated by Django 3.2.15 on 2022-12-03 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_shhouseinfo_tyhouseinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseinfo',
            name='total_price',
            field=models.CharField(max_length=20, verbose_name='售价(万元)'),
        ),
        migrations.AlterField(
            model_name='shhouseinfo',
            name='total_price',
            field=models.CharField(max_length=20, verbose_name='售价(万元)'),
        ),
        migrations.AlterField(
            model_name='tyhouseinfo',
            name='total_price',
            field=models.CharField(max_length=20, verbose_name='售价(万元)'),
        ),
    ]
