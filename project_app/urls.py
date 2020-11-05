
from project_app.views import recipe_details
from project_app.views import edit_recipe
from project_app.views import delete_recipe
from project_app.views import create_recipe
from project_app.views import index
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('details/<int:pk>/', recipe_details, name='recipe details'),
]
