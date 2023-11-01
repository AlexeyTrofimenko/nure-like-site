from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Page


@admin.register(Page)
class PageAdmin(SortableAdminMixin, admin.ModelAdmin):

    prepopulated_fields = {'link': ('name_eng',)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)

        _field_labels = {
            'name_ukr': 'Назва українською',
            'name_eng': 'Назва англійською',
            'link': 'Посилання на сторінку',
            'content_ukr': 'Контент українською',
            'content_eng': 'Контент англійською'
        }

        if formfield:
            formfield.label = _field_labels.get(db_field.name)

        return formfield


admin.site.unregister(Group)
