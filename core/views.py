from django.shortcuts import render, get_object_or_404
from .models import Termo, Capitulo
from django.db.models import Prefetch, Q

# Create your views here.
def home(request):
    return render(request, 'core/home.html', {})

def about(request):
    return render(request, 'core/about.html')

def terms(request):
    capitulos = Capitulo.objects.order_by('titulo').prefetch_related(
        Prefetch(
            'termos',
            queryset=Termo.objects.prefetch_related('definicoes').order_by('titulo')
        )
    )
    return render(request, 'core/terms.html', {'capitulos': capitulos})

def references(request):
    termos = Termo.objects.prefetch_related(
        'definicoes__referencias'
    ).all().order_by('titulo')

    return render(request, 'core/references.html', {
        'termos': termos
    })

def search(request):
    query = request.GET.get('q', '')

    termos = Termo.objects.select_related('capitulo').prefetch_related('definicoes').filter(
        Q(titulo__icontains=query)
    ).order_by('capitulo__titulo', 'titulo') if query else []

    return render(request, 'core/search_results.html', {
        'query': query,
        'termos': termos
    })

def detail(request, id):
    termo = get_object_or_404(Termo.objects.prefetch_related(
        'definicoes__exemplos',
        'definicoes__referencias'
    ), pk=id)
    
    context = {
        'termo': termo
    }
    return render(request, 'core/term.html', context)
