from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhoneNumberCreateView(generics.CreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneSerrializer

    def perform_create(self, serializer):
        # Заполняем поле user текущего аутентифицированного пользователя
        serializer.save(user=self.request.user)

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
    