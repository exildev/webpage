from django.contrib import admin
import models
import forms
# Register your models here.


class SeccionStack(admin.StackedInline):
    model = models.Seccion
    form = forms.SeccionForm

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
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.SubItem, SubitemAdmin)
admin.site.register(models.ItemSeccion)
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.MenuPrincipal, MenuPrincipalAdmin)
admin.site.register(models.PaginaPrincipal, PaginaPrincipalAdmin)
