from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello from django")


def selection_recipes(request):
    context = {
        'header': 'List of dishes',
        'DATA': ['omlet', 'pasta', 'buter', 'russian salad']
    }

    return render(request, 'index.html', context)


def omlet(request):
    servings = int(request.GET.get('servings', 1))
    if servings == 1:
        w = 'я'
    else:
        w = 'и'
    return HttpResponse(
        f'<h2>Ингредиенты для Омлета: {servings} порци{w}</h2>'
        f'<ol><h3>яйца, шт: {2 * servings}</h3></ol>'
        f'<ol><h3>молоко, л: {0.1 * servings}</h3></ol>'
        f'<ol><h3>соль, ч.л.: {0.5 * servings}</h3></ol>'
    )


def pasta(request):
    servings = int(request.GET.get('servings', 1))
    if servings == 1:
        w = 'я'
    else:
        w = 'и'
    return HttpResponse(
        f'<h2>Ингредиенты для Пасты: {servings} порци{w}</h2>'
        f'<ol><h3>макароны, г: {0.3 * servings}</h3></ol>'
        f'<ol><h3>сыр, г: {0.05 * servings}</h3></ol>'
    )
#
def buter(request):
    servings = int(request.GET.get('servings', 1))
    if servings == 1:
        w = 'я'
    else:
        w = 'и'
    return HttpResponse(
        f'<h2>Ингредиенты для Бутерброда: {servings} порци{w}</h2>'
        f'<ol><h3>хлеб ломтик: {1 * servings}</h3></ol>'
        f'<ol><h3>колбаса ломтик: {1 * servings}</h3></ol>'
        f'<ol><h3>сыр ломтик: {1 * servings}</h3></ol>'
          f'<ol><h3>помидор ломтик: {1 * servings}</h3></ol>'
    )

def russian_salad(request):
    servings = int(request.GET.get('servings', 1))
    if servings == 1:
        w = 'я'
    else:
        w = 'и'
    return HttpResponse(
        f'<h2>Ингредиенты для Винегрета: {servings} порци{w}</h2>'
        f'<ol><h3>картошка: {60 * servings}</h3></ol>'
        f'<ol><h3>морковь: {24 * servings}</h3></ol>'
        f'<ol><h3>свекла: {60 * servings}</h3></ol>'
        f'<ol><h3>соленые огурцы: {24 * servings}</h3></ol>'
        f'<ol><h3>консервный горошек: {26 * servings}</h3></ol>'
    )



