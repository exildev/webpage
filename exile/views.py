from django.shortcuts import render
from django.http import Http404
from django.utils.decorators import method_decorator
from supra import views as supra
from django.views.decorators.csrf import csrf_exempt
import models
import forms
# Create your views here.


def index(request):
    principal = models.MenuPrincipal.objects.all().first()
    home = models.PaginaPrincipal.objects.all().first()
    footer = models.FooterPrincipal.objects.all().first()
    # end if
    return render(request, 'exile/index.html', {'contenido': home.pagina, 'menu': principal.menu, 'footer': footer.footer })
# end def


def page(request, alias):
    pagina = models.Page.objects.filter(alias=alias).first()
    if pagina:
        principal = models.MenuPrincipal.objects.all().first()
        footer = models.FooterPrincipal.objects.all().first()
        # end if
        return render(request, 'exile/page.html', {'contenido': pagina, 'menu': principal.menu, 'footer': footer.footer })
    # end if
    raise Http404("Poll does not exist")
# end def


class ContactoSupra(supra.SupraFormView):
    model = models.Contacto
    form_class = forms.ContactoForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ContactoSupra, self).dispatch(request, *args, **kwargs)
    # end def
# end class
