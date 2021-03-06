from django import forms
from django.template.loader import render_to_string
from django.contrib.admin.widgets import FilteredSelectMultiple


class PopUpBaseWidget(object):
    def __init__(self, model=None, template='addnew.html', *args, **kwargs):
        self.model = model
        self.template = template
        super(PopUpBaseWidget, self).__init__(*args, **kwargs)

    def render(self, name, *args, **kwargs):
        html = super(PopUpBaseWidget, self).render(name, *args, **kwargs)

        if not self.model:
            self.model = name

        popupplus = render_to_string(self.template, {'field': name, 'model': self.model})
        return html+popupplus

    def _media(self):
        js = ["admin/js/core.js", "admin/js/admin/RelatedObjectLookups.js"]

        return forms.widgets.Media(
            js=js
        )
    media = property(_media)


class FilteredMultipleSelectWithPopUp(PopUpBaseWidget, FilteredSelectMultiple):
    pass


class MultipleSelectWithPopUp(PopUpBaseWidget, forms.SelectMultiple):
    pass


class SelectWithPopUp(PopUpBaseWidget, forms.Select):
    pass
