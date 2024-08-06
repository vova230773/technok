from django.contrib import admin

from operation.models import oper_mod


@admin.register(oper_mod)
class oper_mod_modAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]