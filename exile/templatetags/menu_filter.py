from django.template import Library
from exile import models
register = Library()


@register.filter(name="items_tag")
def ordenItem(menu):
    return menu.items.all().order_by('ordenitem__posicion')
# end def


@register.filter(name="subitems_tag")
def ordenSubItem(item, seccion):
    if seccion:
        return item.subitems.all().filter(ordensubitem__seccion=seccion).order_by('ordensubitem__posicion')
    # end if
    return item.subitems.all().order_by('ordensubitem__posicion')
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
            if secciones.count(orden.seccion) == 0:
                secciones.append(orden.seccion)
            # end if
    # end if
    return secciones
# end def


@register.filter(name="footerSeccion_tag")
def footerSeccion(footer):
    secciones = []
    for f in footer.paginas.all():
        orden = models.OrdenFooter.objects.filter(footer=footer, page=f)
        if secciones.count(orden.seccion) == 0:
            secciones.append(orden.seccion)
        # end if
    # end for
    return secciones
# end def


@register.filter(name="footerPage_tag")
def footerPage(footer, seccion):
    return footer.paginas.all().filter(ordenfooter__seccion=seccion).order_by('posicion')
# end def


@register.filter(name="col_num")
def colNum(total, col):
    if total == 0:
        num = col
    else:
        num = col/total
    # end if
    return num
# end def
