from django.contrib import admin

# Register your models here.
from .models import *


class StockAdmin(admin.ModelAdmin):
    list_display = ["category", "stock_name", "quantity"]
    list_filter = ["stock_name"]
    search_fields = ["category", "stock_name"]


admin.site.register(Stock, StockAdmin)
admin.site.register(Category)
admin.site.site_header = "Sales Dashboard"
admin.site.site_title = "Sales Dashboard"
