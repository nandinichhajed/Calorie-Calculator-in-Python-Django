from django.contrib import admin
from . models import *
# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    class Meta:
        model = FoodItem
    list_display = ['name']
    list_filter = ['name']

admin.site.register(Customer)
admin.site.register(UserFoodItem)
admin.site.register(Category)
admin.site.register(FoodItem,FoodAdmin)