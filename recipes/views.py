
# from rest_framework import generics
# from .models import Recipe
# from .serializers import RecipeSerializer
# from django.http import HttpResponse
# import logging
# from rest_framework.response import Response
# from rest_framework import status

# logger = logging.getLogger(__name__)

# class RecipeListCreate(generics.ListCreateAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer

#     def create(self, request, *args, **kwargs):
#         try:
#             return super().create(request, *args, **kwargs)
#         except Exception as e:
#             logger.error(f"Error creating recipe: {e}")
#             return Response({'error': 'An error occurred while adding the recipe.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class RecipeDelete(generics.DestroyAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer        

# def index(request):
#     return HttpResponse("Hello, this is your Django backend.")

from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer
from django.http import HttpResponse
import logging
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error creating recipe: {e}")
            return Response({'error': 'An error occurred while adding the recipe.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RecipeDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer        

def index(request):
    return HttpResponse("Hello, this is your Django backend.")