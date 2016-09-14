#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from suit_ckeditor.widgets import CKEditorWidget
import models


class SeccionForm(forms.ModelForm):

    class Meta:
        model = models.Seccion
        exclude = ()
        widgets = {
         'contenido': CKEditorWidget(editor_options={'lang': 'es', 'startupFocus': True})
        }
    # end class
# end class
