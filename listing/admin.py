from django.contrib import admin
from .models import Listing,OrderItem,Order

admin.site.register(Listing)
admin.site.register(Order)
admin.site.register(OrderItem)
