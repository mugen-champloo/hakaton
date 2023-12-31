# Generated by Django 4.2.5 on 2023-09-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_order_complied'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients_for_cook_quantity',
            field=models.CharField(blank=True, verbose_name='Ингредиенты для готовки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients_for_cook',
            field=models.CharField(blank=True, verbose_name='Ингредиенты для готовки'),
        ),
    ]
