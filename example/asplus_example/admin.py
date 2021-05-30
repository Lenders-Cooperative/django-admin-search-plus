from django.contrib import admin
from asplus_example.models import SomeModel
from admin_search_plus import AdminSearchPlusMixin


class SomeModelAdmin(AdminSearchPlusMixin, admin.ModelAdmin):
    search_fields = ['field_1', 'field_2', 'field_3']


admin.site.register(SomeModel, SomeModelAdmin)
