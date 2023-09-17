from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/products/', GetProductinfo.as_view()),
    path('api/prodcat/', GetProductCategoryInfo.as_view()),
    path('api/recipes/', GetRecipeInfo.as_view(), name='what_is_this'),
    path('api/reccat/', GetRecipeCategory.as_view(), name='abracadabra'),
    path('api/products/by_category/<int:category_id>', ProductListByCategory.as_view(), name='product-list-by-category')
]
