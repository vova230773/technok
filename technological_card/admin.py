from django.contrib import admin

from technological_card.models import tk_mod


@admin.register(tk_mod)
class tk_modAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("name",)}
    list_display = ["product",]
