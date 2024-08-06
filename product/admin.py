from dataclasses import field
from django.contrib import admin
from core.models import Counterparts,contrgrupp,licenss,Priv

from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget

from product.models import product_mod


@admin.register(product_mod)
class product_modAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]