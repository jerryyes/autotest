# Generated by Django 2.0.2 on 2019-06-11 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190611_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productname',
            field=models.CharField(max_length=64, verbose_name='产品名称'),
        ),
    ]
