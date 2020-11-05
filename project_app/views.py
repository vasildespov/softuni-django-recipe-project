from project_app.forms import DeleteRecipeForm
from project_app.models import Recipe
from project_app.forms import RecipeForm
from django.shortcuts import redirect, render


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        context = {
            'form': RecipeForm(),
        }
        return render(request, 'create.html', context)
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': RecipeForm(instance=recipe),
        }
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            "recipe": recipe,
            "form": DeleteRecipeForm(instance=recipe),
        }
        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('index')


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(',')
    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'ingredients': ingredients,
        }
        return render(request, 'details.html', context)
