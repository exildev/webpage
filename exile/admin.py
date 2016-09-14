from django.contrib import admin
import models
import forms
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    form = forms.PageForm
# end class

admin.site.register(models.Page, PageAdmin)
admin.site.register(models.Seccion)
admin.site.register(models.OrdenPagina)
admin.site.register(models.Menu)
admin.site.register(models.OrdenSeccion)
admin.site.register(models.MenuPrincipal)
