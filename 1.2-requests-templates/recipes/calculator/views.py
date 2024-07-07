from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def index(request):
    template_name = 'calculator/index.html'
    context = DATA
    return render(request, template_name, context)


def count_servings(request, context):
    if 'servings' in request.GET:
        count = int(request.GET['servings'])
        for ingredient, amount in context['recipe'].items():
            context['recipe'][ingredient] = amount * count
    return context


def omlet_view(request):
    template_name = 'calculator/index.html'
    context = {
        'recipe': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        }
    }
    count_servings(request, context)
    return render(request, template_name, context)


def pasta_view(request):
    template_name = 'calculator/index.html'
    context = {
        'recipe': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        }
    }
    count_servings(request, context)
    return render(request, template_name, context)


def buter_view(request):
    template_name = 'calculator/index.html'
    context = {
        'recipe': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        }
    }
    count_servings(request, context)
    return render(request, template_name, context)
