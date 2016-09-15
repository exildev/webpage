from markdownx.widgets import AdminMarkdownxWidget
from django.contrib import admin
from django.db import models as model
import models
import forms
# Register your models here.


class SeccionStack(admin.StackedInline):
    model = models.Seccion
    #formfield_overrides = {
    #  model.TextField: {'widget': AdminMarkdownxWidget},
    #}

    fieldsets = [
       (None, {'fields': ['nombre', 'posicion']}),
       ('Editor', {
           'classes': ('full-width',),
           'description': 'Escribir su codigo html aqui',
           'fields': ['contenido']})]

    class Media:
        js = ('exile/js/jquery-2.1.1.min.js',)
    # end class
# end class


class SeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pagina', 'posicion')
    search_fields = ('nombre',)
    list_filter = ('pagina', )
    formfield_overrides = {
       model.TextField: {'widget': AdminMarkdownxWidget},
    }

    class Media:
        js = ('exile/jquery-2.1.1.min.js',)
    # end class
# end class


class PageAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    inlines = [
        SeccionStack,
    ]
# end class


class OrdenSubItemStack(admin.StackedInline):
    model = models.OrdenSubItem
# end class


class ItemAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'principal')
    search_fields = ('nombre', )
    inlines = [
        OrdenSubItemStack,
    ]
# end class


class OrdenItem(admin.StackedInline):
    model = models.OrdenItem
# end class


class MenuAdmin(admin.ModelAdmin):
    inlines = [
        OrdenItem,
    ]
# end class


class SubitemAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pagina')
# end class


class MenuPrincipalAdmin(admin.ModelAdmin):
    list_display = ('menu', 'fecha')
# end class


class PaginaPrincipalAdmin(admin.ModelAdmin):
    list_display = ('pagina', 'fecha')
# end class


admin.site.register(models.Page, PageAdmin)
admin.site.register(models.Seccion, SeccionAdmin)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.SubItem, SubitemAdmin)
admin.site.register(models.ItemSeccion)
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.MenuPrincipal, MenuPrincipalAdmin)
admin.site.register(models.PaginaPrincipal, PaginaPrincipalAdmin)
