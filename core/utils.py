from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

SEIS_MESES = 1
UM_ANO = 2
DOIS_ANOS = 2
TRES_ANOS = 3
QUATRO_ANOS = 4
MAIS_DE_QUATRO_ANOS = 5
LIST_EXPERIENCIA = (
    (SEIS_MESES, '6 Meses'),
    (UM_ANO, '1 ano'),
    (DOIS_ANOS, '2 anos '),
    (TRES_ANOS, '3 anos '),
    (QUATRO_ANOS, '4 anos '),
    (MAIS_DE_QUATRO_ANOS, '5 anos ou mais '),
)

DEFAULT = 0
SUPERIOR_COMPLETO = 1
SUPERIOR_CURSANDO = 2
NIVEL_TECNICO = 3
SEGUNDO_GRAU_COMPLETO = 4
SEGUNDO_GRAU_CURSANDO = 5
LIST_ESCOLARIDADE = (
    (DEFAULT, '-------------'),
    (SUPERIOR_COMPLETO, 'Ensino superior completo'),
    (SUPERIOR_CURSANDO, 'Ensino superior cursando'),
    (NIVEL_TECNICO, 'Nivel Tecnico'),
    (SEGUNDO_GRAU_COMPLETO, 'Segundo Grau completo '),
    (SEGUNDO_GRAU_CURSANDO, 'Segundo Grau cursando'),
)


def paginator(request, object_list, por_page=5):
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    pages = Paginator(object_list, por_page)
    objects_paginated = pages.page(page)
    return objects_paginated
