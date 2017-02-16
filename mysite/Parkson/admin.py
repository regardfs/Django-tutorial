from django.contrib import admin
from Parkson.models import Parkson, Food

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')
    search_fields = ('name',)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')
    list_filter = ('favourite',)
    fields = ('price', 'restaurant')
    ordering = ('-price',)

admin.site.register(Parkson, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
