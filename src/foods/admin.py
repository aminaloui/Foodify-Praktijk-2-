from django.contrib import admin

# Register your models here.
from .models import Food, Thumbnail


class ThumbnailInline(admin.TabularInline):
    extra = 0
    model = Thumbnail


class FoodAdmin(admin.ModelAdmin):
    inlines = [ThumbnailInline]
    list_display = ["__unicode__","description","price"]
    search_fields = ["title","description","price"]
    list_filter = ["price"]
    prepopulated_fields = {"slug": ("title",)} #maakt slug field gelijk aan titel wanneer slug leeg is.
    class Meta:
        model = Food


admin.site.register(Food, FoodAdmin)


admin.site.register(Thumbnail)
