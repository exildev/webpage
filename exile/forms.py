#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import EmailMultiAlternatives
import models
from ace_overlay.widgets import AceOverlayWidget


class SeccionForm(forms.ModelForm):

    class Meta:
        model = models.Seccion
        exclude = ()
        widgets = {
            "contenido": AceOverlayWidget(mode='html', wordwrap=False, theme='monokai', width="100%", height="400px", showprintmargin=False)
        }
    # end class
# end class


class ContactoForm(forms.ModelForm):

    class Meta:
        model = models.Contacto
        exclude = ()
    # end class

    def save(self, commit=True):
        contacto = super(ContactoForm, self).save(commit)
        subject, from_email, to = contacto.asunto, contacto.email, 'info@exile.com.co'
        text_content = "Mensaje de Contacto"
        html_content = "<p>Correo: %s</p><p>Telefono: %s</p><p>Mensaje:, %s </p>" % (contacto.email, contacto.telefono, contacto.mensaje)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return contacto
    # end def
# end class
