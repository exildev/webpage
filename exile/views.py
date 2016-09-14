from django.shortcuts import render
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
