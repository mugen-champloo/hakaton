from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.generics import ListAPIView


from .serializers import *
from .models import *


# все продукты
class GetProductinfo(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer_for_queryset = ProductSerializers(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)


# все категории продукта
class GetProductCategoryInfo(APIView):
    def get(self, request):
        queryset = ProductCategory.objects.all()
        s = CategorySerializer(queryset, many=True)
        return Response(s.data)


class ProductListByCategory(ListAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category=category_id)
    


class GetRecipeInfo(ListAPIView):
    queryset = Recipe
    serializer_class = RecipeSerializer

    def get_queryset(self):
        return Recipe.objects.all()
    

class GetRecipeCategory(ListAPIView):
    queryset = RecipeCategory
    serializer_class = CategoryRecipeSerializer

    def get_queryset(self):
        return RecipeCategory.objects.all()
    