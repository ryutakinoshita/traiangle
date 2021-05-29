from django.db import models

from accounts.models import User
from accountsDetail.models import Producer
from config import settings
from django.utils import timezone

class Type(models.Model):
    TypeListing=(
        ("1", "野菜"),
        ("2", "果物"),
        ("3", "鮮魚"),
        ("4", "食肉"),
        ("5", "乳製品"),
        ("6", "加工食品"),
        ("7", "飲料"),
        ("9", "アルコール飲料"),
        ("10", "園芸"),
        ("11", "その他"),
    )

class Listing(models.Model):
    listing_user=models.ForeignKey(Producer, on_delete=models.CASCADE)
    listing_img1= models.ImageField(upload_to='listingImg')
    listing_img2= models.ImageField(upload_to='listingImg')
    listing_img3= models.ImageField(upload_to='listingImg')
    listing_type =models.CharField(max_length=100, choices=Type.TypeListing, blank=True, null=False)
    listing_name=models.CharField(max_length=100,blank=True, null=False)
    listing_text=models.TextField(max_length=500,blank=True, null=True)
    listing_price=models.IntegerField(blank=True, null=True)
    slug=models.SlugField()


    def __str__(self):
            return self.listing_name


class OrderItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    item=models.ForeignKey(Listing,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)


    def get_total_item_price(self):
        return self.quantity * self.item.listing_price *1.1


    def __str__(self):
        return f'{self.item.listing_name}:{self.quantity}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    start_date=models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def get_total(self):
        total=0
        for order_item in self.items.all():
            total+=order_item.get_total_item_price()
        return total

    def __str__(self):
        return self.user.email


class Payment(models.Model):
    user = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    stripe_charge_id = models.CharField(max_length=50)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email