#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from suit_redactor.widgets import RedactorWidget
import models


class PageForm(forms.ModelForm):

    class Meta:
        model = models.Page
        exclude = ()
        widgets = {
         'contenido': RedactorWidget(editor_options={'lang': 'es'})
        }
    # end class
# end class
