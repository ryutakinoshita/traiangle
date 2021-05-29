from django.contrib import admin
from .models import Producer, Restaurant, RestaurantImage

admin.site.register(Producer)
admin.site.register(Restaurant)
admin.site.register(RestaurantImage)

