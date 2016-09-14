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
    contenido = models.TextField()

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"
    # end class
# end class


class Item(models.Model):
    nombre = models.CharField(max_length=400)
    principal = models.ForeignKey(Page, blank=True, null=True, verbose_name="Pagina Principal")

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Item's"
    # end class

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class OrdenPagina(models.Model):
    item = models.ForeignKey(Item)
    posicion = models.IntegerField()
    pagina = models.ForeignKey(Page)

    class Meta:
        verbose_name = "Orden de la pagina"
        verbose_name_plural = "Orden de las paginas"
    # end class

    def __unicode__(self):
        return u"%s pagina: %s" % (self.item.nombre, self.pagina.nombre)
    # end def
# end class


class Menu(models.Model):
    nombre = models.CharField(max_length=400)

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class OrdenItem(models.Model):
    menu = models.ForeignKey(Menu)
    posicion = models.IntegerField()
    item = models.ForeignKey(Item)

    class Meta:
        verbose_name = "Orden de item"
        verbose_name_plural = "Orden de items"
    # end class

    def __unicode__(self):
        return u"%s item: %s" % (self.menu.nombre, self.seccion.nombre)
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
