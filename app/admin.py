from django.contrib import admin
from app.models import StripeCustomer,Withdrawal



admin.site.register(StripeCustomer)
admin.site.register(Withdrawal)

