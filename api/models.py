from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group as AuthGroup
from .validators import *


class PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Номер телефона', validators=[validate_phone_number])

    def __str__(self):
        return self.phone_number
    


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    category = models.ForeignKey('ProductCategory', null=True, on_delete=models.SET_NULL, verbose_name='Категория')
    image = models.CharField(max_length=300, null=True, verbose_name='ссылка на картинку')
    unit = models.CharField(max_length=100, verbose_name='Единица измерения')
    quantity = models.FloatField(verbose_name='Количество за ед.измерения')
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
    ingredients_for_cook = models.CharField(blank=True, verbose_name='Ингредиенты для готовки')
    ingredients_for_cook_quantity = models.CharField(blank=True, verbose_name='Ингредиенты для готовки')

    def __str__(self):
        return self.name


class RecipeCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория блюд')
    image = models.CharField(max_length=300, null=True, verbose_name='ссылка на картинку')

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=50, verbose_name='Номер заказа')
    time_ordered = models.DateTimeField(auto_now_add=True, verbose_name='Во сколько заказали')
    adress = models.CharField(max_length=100, verbose_name='Адресс доставки')
    complied = models.BooleanField(default=False)


class OrederItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='id заказа')
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, verbose_name="id продкта")
    quantity = models.FloatField(default=1, verbose_name='Количество выбранного товара')
