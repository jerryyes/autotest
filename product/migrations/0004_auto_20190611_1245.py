# Generated by Django 2.0.2 on 2019-06-11 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190611_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productname',
            field=models.CharField(max_length=200, verbose_name='产品名称'),
        ),
    ]
