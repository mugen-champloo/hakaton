from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    category = models.ForeignKey('ProductCategory', null=True,on_delete=models.SET_NULL, verbose_name='Категория')
    image = models.CharField(max_length=300, null=True, verbose_name='ссылка на картинку')
    unit = models.CharField(max_length=100, verbose_name='Единица измерения')
    quantity = models.IntegerField(verbose_name='Количество за ед.измерения')
    price = models.IntegerField(verbose_name='Цена')
    in_stock = models.BooleanField(default=False, verbose_name='В наличии')

    def __str__(self):
        return self.name
    

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование категории')
    image = models.CharField(max_length=300, null=True, verbose_name='ссылка на картинку')

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименования блюда')
    text = models.TextField(max_length=300, verbose_name='Описание')
    ingredients = models.ManyToManyField(Product, verbose_name='продукты')
    image = models.CharField(max_length=300, null=True, verbose_name='ссылка на картинку')
    cooking_time = models.CharField(max_length=50, verbose_name='Время готовки')
    energy = models.IntegerField(verbose_name='Энергетическая ценность')
    portion = models.CharField(max_length=50, verbose_name='На сколько человек')
    how_to_cook = models.TextField(max_length=300, verbose_name="Способ приготовления")
    ingredients_for_cook = models.JSONField(blank=True, verbose_name='Ингредиенты для готовки')

    def __str__(self):
        return self.name


class RecipeCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория блюд')
    image = models.CharField(max_length=300, null=True, verbose_name='ссылка на картинку')

    def __str__(self):
        return self.name
