#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Page(models.Model):
    nombre = models.CharField(max_length=400)

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
    # end class

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Seccion(models.Model):
    pagina = models.ForeignKey(Page)
    nombre = models.CharField(max_length=400)
    posicion = models.IntegerField()
    contenido = models.TextField()

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"
    # end class
# end class


class ItemSeccion(models.Model):
    nombre = models.CharField(max_length=400)

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class SubItem(models.Model):
    nombre = models.CharField(max_length=400)
    pagina = models.ForeignKey(Page)

    class Meta:
        verbose_name = "SubItem"
        verbose_name_plural = "SubItem's"
    # end class

    def __unicode__(self):
        return u"%s pagina: %s" % (self.nombre, self.pagina.nombre)
    # end def
# end class


class OrdenSubItem(models.Model):
    subitem = models.ForeignKey(SubItem)
    item = models.ForeignKey('Item')
    posicion = models.IntegerField()
    seccion = models.ForeignKey(ItemSeccion, blank=True, null=True)

    class Meta:
        verbose_name = "Orden de subitem"
        verbose_name_plural = "Ordenes de subitem"
    # end class
# end class


class Item(models.Model):
    nombre = models.CharField(max_length=400)
    principal = models.ForeignKey(Page, blank=True, null=True, verbose_name="Pagina Principal")
    subitems = models.ManyToManyField(SubItem, through=OrdenSubItem)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Item's"
    # end class

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class OrdenItem(models.Model):
    menu = models.ForeignKey('Menu')
    posicion = models.IntegerField()
    item = models.ForeignKey(Item)

    class Meta:
        verbose_name = "Orden de item"
        verbose_name_plural = "Orden de items"
    # end class

    def __unicode__(self):
        return u"%s item: %s" % (self.menu.nombre, self.item.nombre)
    # end def
# end class


class Menu(models.Model):
    nombre = models.CharField(max_length=400)
    items = models.ManyToManyField(Item, through=OrdenItem)

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class MenuPrincipal(models.Model):
    menu = models.OneToOneField(Menu)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Menu principal"
        verbose_name_plural = "Menu principal"
    # end class

    def __unicode__(self):
        return u"%s" % (self.menu.nombre)
# end class


class PaginaPrincipal(models.Model):
    pagina = models.OneToOneField(Page)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Pagina principal"
        verbose_name_plural = "Pagina principal"
    # end class

    def __unicode__(self):
        return u"%s" % (self.pagina.nombre)
# end class


class Contacto(models.Model):
    nombre = models.CharField(max_length=300)
    email = models.EmailField()
    asunto = models.CharField(max_length=300)
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()

    def __unicode__(self):
        return u"%s %s" % (self.nombre, self.email)
    # end def
# end class


class SeccionFooter(models.Model):
    nombre = models.CharField(max_length=400)

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class OrdenFooter(models.Model):
    pagina = models.ForeignKey(Page)
    seccion = models.ForeignKey(SeccionFooter)
    posicion = models.IntegerField()
    footer = models.ForeignKey('Footer')


class Footer(models.Model):
    nombre = models.CharField(max_length=300)
    paginas = models.ManyToManyField(Page, through=OrdenFooter)

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class FooterPrincipal(models.Model):
    footer = models.OneToOneField(Footer)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Footer Principal"
        verbose_name_plural = "Footer Principal"
    # end class

    def __unicode__(self):
        return u"%s" % (self.footer.nombre)
    # end def
# end class
