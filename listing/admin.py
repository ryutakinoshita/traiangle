from django.contrib import admin
from .models import Listing,OrderItem,Order,Payment

admin.site.register(Listing)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)