from django.template import Library
from exile import models
register = Library()


@register.filter(name="items_tag")
def ordenItem(menu):
    return menu.items.all().order_by('ordenitem__posicion')
# end def


@register.filter(name="contenido_tag")
def ordernContenido(page):
    secciones = models.Seccion.objects.filter(pagina=page).order_by('posicion')
    print secciones
    return secciones
# end def


def subItemsSeccion(subitems):
    secciones = models.ItemSeccion.objects.all()
    return
# end def
