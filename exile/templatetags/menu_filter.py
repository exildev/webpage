from django.template import Library
from exile import models
register = Library()


@register.filter(name="items_tag")
def ordenItem(menu):
    return menu.items.all().order_by('ordenitem__posicion')
# end def


@register.filter(name="subitems_tag")
def ordenSubItem(item, seccion):
    return item.subitems.all().filter(ordensubitem__seccion=seccion).order_by('ordensubitem__posicion')
# end def


@register.filter(name="contenido_tag")
def ordernContenido(page):
    secciones = models.Seccion.objects.filter(pagina=page).order_by('posicion')
    return secciones
# end def


@register.filter(name="subseccion_tag")
def subItemsSeccion(item):
    secciones = []
    for s in item.subitems.all():
        orden = models.OrdenSubItem.objects.filter(item=item, subitem=s).first()
        if orden.seccion:
            if secciones.count(orden.seccion.nombre) == 0:
                secciones.append(orden.seccion)
            # end if
    # end if
    return secciones
# end def


@register.filter(name="col_num")
def colNum(total, col):
    if total == 0:
        num = col
    else:
        num = col/total
    # end if
    return col
# end def
