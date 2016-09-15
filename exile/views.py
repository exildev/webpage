from django.shortcuts import render
from django.http import Http404
import models
# Create your views here.


def index(request):
    principal = models.MenuPrincipal.objects.all().first()
    home = models.PaginaPrincipal.objects.all().first()
    # end if
    return render(request, 'exile/index.html', {'contenido': home.pagina, 'menu': principal.menu})
# end def


def page(request, id):
    pagina = models.Page.objects.filter(id=id).first()
    if pagina:
        principal = models.MenuPrincipal.objects.all().first()
        items = []
        if principal:
            items = models.OrdenItem.objects.filter(menu=principal.menu).first()
        # end if
        return render(request, 'exile/page.html', {'contenido': pagina, 'items': items})
    # end if
    raise Http404("Poll does not exist")
# end def
