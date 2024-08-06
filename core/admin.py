from dataclasses import field
from django.contrib import admin
from core.models import Counterparts,contrgrupp,licenss,Priv

from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget

from product.models import product_mod

class CounterpartsResource(resources.ModelResource):
    
    class Meta:

        model=Counterparts

class CounterpartsAdmin(ImportExportModelAdmin):
    resource_classe=CounterpartsResource
    list_display = [
        "name",
        "full_name",
        "adres",
        "okpo_cod",
        "group",
     
    ]
    prepopulated_fields={
        'slug':('name',)}
    # list_display=[field.name for field in Counterparts._meta.fields if field.name !='id']
    search_fields = ["name", "okpo_cod"]
    

admin.site.register(Counterparts,CounterpartsAdmin)



    
@admin.register(contrgrupp)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]

@admin.register(Priv)
class PrivAdmin(admin.ModelAdmin):
   
    list_display = ["grup","us"]

# @admin.register(licenss)
# class licenssAdmin(admin.ModelAdmin):
    
#     list_display = ["contragent","data_po","create_at","guid",]

#     def create_time_display(self, obj):
#         return obj.create_time.strftime("%B %d, %Y")

#     create_time_display.data_po = 'дата по'

class licenssResource(resources.ModelResource):
    
    class Meta:

        model=licenss

class licenssAdmin(ImportExportModelAdmin):
    resource_classe=licenssResource
    list_display = [
        "contragent","data_po","create_at","guid",
     
    ]
    
    search_fields = ["contragent", "data_po"]
    

admin.site.register(licenss,licenssAdmin)

