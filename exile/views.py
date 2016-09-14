from django.shortcuts import render
import models
# Create your views here.


def index(request):
    return render(request, 'exile/index.html', {})
# end def
