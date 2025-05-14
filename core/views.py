from django.shortcuts import render
from .models import Term

# Create your views here.
def home(request):
    return render(request, 'core/home.html', {})

def search(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        results = Term.objects.filter(name__icontains=query)

    return render(request, 'core/search_results.html', {
        'query': query,
        'results': results,
    })

def detail(request, id):
    term = Term.objects.get(id=id)
    return render(request, 'core/detail.html', {'term': term})