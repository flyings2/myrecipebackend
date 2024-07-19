# from django.urls import path
# from .views import RecipeListCreate, index, RecipeDelete

# urlpatterns = [
#     path('recipes/', RecipeListCreate.as_view(), name='recipe-list-create'),
#     path('recipes/<int:pk>/', RecipeDelete.as_view(), name='recipe-delete'),
#     path('', index, name='index'),
# ]

from django.urls import path
from .views import RecipeListCreate, RecipeDetailUpdateDelete, index

urlpatterns = [
    path('recipes/', RecipeListCreate.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetailUpdateDelete.as_view(), name='recipe-detail-update-delete'),
    path('', index, name='index'),
]