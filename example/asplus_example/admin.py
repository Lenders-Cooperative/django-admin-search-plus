from django.contrib import admin
from asplus_example.models import SomeModel
from admin_search_plus import AdminSearchPlusMixin


class SomeModelAdmin(AdminSearchPlusMixin, admin.ModelAdmin):
    admin_search_plus = True
    show_full_result_count = True
    show_result_count = True
    search_fields = ['field_1', 'field_2', 'field_3']


admin.site.register(SomeModel, SomeModelAdmin)
