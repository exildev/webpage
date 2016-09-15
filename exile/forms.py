#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from suit_ckeditor.widgets import CKEditorWidget
import models


class SeccionForm(forms.ModelForm):

    class Meta:
        ck_editor_toolbar = [
            {'name': 'basicstyles', 'groups': ['basicstyles', 'cleanup']},
            {'name': 'paragraph',
                'groups': ['list', 'indent', 'blocks', 'align']},
            {'name': 'document', 'groups': ['mode']}, '/',
            {'name': 'styles'}, {'name': 'colors'},
            {'name': 'insert_custom',
                'items': ['Image', 'Flash', 'Table', 'HorizontalRule']},
            {'name': 'about'}]
        ck_editor_config = {'autoGrow_onStartup': True, 'autoGrow_minHeight': 100,
                            'autoGrow_maxHeight': 250, 'extraPlugins': 'autogrow', 'toolbarGroups': ck_editor_toolbar}
        model = models.Seccion
        exclude = ()
        widgets = {
            'contenido': CKEditorWidget(editor_options=ck_editor_config)
        }
    # end class
# end class
