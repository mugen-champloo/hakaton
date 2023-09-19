from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # Импорт представления для получения токена

from .views import *

urlpatterns = [
    path('api/products/', GetProductinfo.as_view()),
    path('api/prodcat/', GetProductCategoryInfo.as_view()),
    path('api/recipes/', GetRecipeInfo.as_view(), name='what_is_this'),
    path('api/reccat/', GetRecipeCategory.as_view(), name='abracadabra'),
    path('api/register/', RegisterUser.as_view(), name='register'),
    path('api/addphone/', RegisterPhone.as_view(), name='add_phone_number'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/products/by_category/<int:category_id>', ProductListByCategory.as_view(), name='product-list-by-category')
]
