# Generated by Django 4.2.5 on 2023-09-17 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=300, null=True, verbose_name='ссылка на картинку'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='image',
            field=models.CharField(max_length=300, null=True, verbose_name='ссылка на картинку'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.CharField(max_length=300, null=True, verbose_name='ссылка на картинку'),
        ),
        migrations.AlterField(
            model_name='recipecategory',
            name='image',
            field=models.CharField(max_length=300, null=True, verbose_name='ссылка на картинку'),
        ),
    ]
