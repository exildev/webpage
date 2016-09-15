#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from tinymce.widgets import TinyMCE
import models


class SeccionForm(forms.ModelForm):

    class Meta:
        model = models.Seccion
        exclude = ()
        widgets = {
            'contenido': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }
    # end class
# end class
