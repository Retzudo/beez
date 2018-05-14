from django.shortcuts import render

from core.models import Apiary, Hive


def search(request):
    query = request.GET.get('q')

    apiaries = Apiary.search(query)
    hives = Hive.search(query)

    return render(request, 'frontend/search.html', {
        'apiaries': apiaries,
        'hives': hives,
    })
