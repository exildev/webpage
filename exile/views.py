from django.shortcuts import render
from django.http import Http404
import models
# Create your views here.


def index(request):
    principal = models.MenuPrincipal.objects.all().first()
    items = []
    if principal:
        items = models.OrdenItem.objects.filter(menu=principal.menu).first()
    # end if
    return render(request, 'exile/index.html', {'items': items})
# end def


def page(request, id):
    pagina = models.Page.objects.filter(id=id).first()
    if pagina:
        return render(request, 'exile/page.html', {'contenido': pagina})
    # end if
    raise Http404("Poll does not exist")
# end def
