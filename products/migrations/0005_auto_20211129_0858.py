# Generated by Django 3.2.8 on 2021-11-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20211124_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(
                blank=True, default='', max_length=254, null=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(
                blank=True, default='', max_length=254, null=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(
                blank=True, default='', max_length=1024, null=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(
                blank=True, default='', max_length=254, null=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='friendly_name',
            field=models.CharField(
                blank=True, default='', max_length=254, null=''),
            preserve_default=False,
        ),
    ]
