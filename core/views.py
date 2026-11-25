
from django.shortcuts import render
from .models import Livro, Autor, Genero
from django.core.paginator import Paginator


def listar_livros(request):

    pesquisa = request.GET.get('pesquisatitulo', '')
    pesquisados = request.GET.get('pesquisaautor', '')
    autor_id = request.GET.get('autor', '')
    genero_id = request.GET.get('genero', '')

    livros = Livro.objects.all().order_by('titulo')

    if pesquisa:
        livros = livros.filter(titulo__icontains=pesquisa)

    if pesquisados:
        livros = livros.filter(autor__nome__icontains=pesquisados)

    if autor_id:
        livros = livros.filter(autor_id=autor_id)

    if genero_id:
        livros = livros.filter(genero_id=genero_id)

    paginator = Paginator(livros, 5)
    pagina = request.GET.get('page')
    page_obj = paginator.get_page(pagina)

    autores = Autor.objects.all().order_by('nome')
    generos = Genero.objects.all().order_by('nome')

    context = {
        'livros': livros,
        'page_obj': page_obj,
        'pesquisa': pesquisa,
        'pesquisados': pesquisados,
        'autores': autores,
        'generos': generos,
        'autor_id': autor_id,
        'genero_id': genero_id,
    }

    return render(request, 'core/livros.html', context)
