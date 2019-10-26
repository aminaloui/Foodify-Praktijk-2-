from django.contrib import admin

# Register your models here.
from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","description","price"]
    search_fields = ["title","description","price"]
    list_filter = ["price"]
    class Meta:
        model = Food

admin.site.register(Food, FoodAdmin)