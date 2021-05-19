from django.contrib import admin
from .models import Producer, Restaurant, RestaurantImage, Individual

admin.site.register(Individual)
admin.site.register(Producer)
admin.site.register(Restaurant)
admin.site.register(RestaurantImage)

