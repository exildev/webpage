#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
import models


class SeccionForm(forms.ModelForm):

    class Meta:
        model = models.Seccion
        exclude = ()
    # end class
# end class
