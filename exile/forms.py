#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from suit_redactor.widgets import RedactorWidget
import models


class SeccionForm(forms.ModelForm):

    class Meta:
        model = models.Seccion
        exclude = ()
        widgets = {
            'contenido': RedactorWidget
        }
    # end class
# end class
