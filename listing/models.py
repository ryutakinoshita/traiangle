from django.db import models
from autoslug import AutoSlugField
from accounts.models import User
from django.utils import timezone
from django.urls import reverse


class Type(models.Model):
    TypeListing=(
        ("1", "野菜"),
        ("2", "果物"),
        ("3", "鮮魚"),
        ("4", "食肉"),
        ("5", "乳製品"),
        ("6", "加工食品"),
        ("7", "飲料"),
        ("8", "アルコール飲料"),
        ("9", "調理済み製品"),
        ("10", "その他"),
    )


class Listing(models.Model):
    """出品モデル"""
    listing_user=models.ForeignKey(User, on_delete=models.CASCADE)
    listing_img1= models.ImageField(upload_to='listingImg',blank=False, null=False)
    listing_img2= models.ImageField(upload_to='listingImg',blank=True, null=True)
    listing_img3= models.ImageField(upload_to='listingImg',blank=True, null=True)
    listing_type =models.CharField(max_length=100, choices=Type.TypeListing, blank=False, null=False)
    listing_name=models.CharField(max_length=100,blank=False, null=False)
    listing_text=models.TextField(max_length=500,blank=True, null=True)
    listing_price=models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    like = models.ManyToManyField(User, related_name='related_post', blank=True)
    slug=AutoSlugField(populate_from='listing_name',null=False, unique=True)



    def __str__(self):
            return self.listing_name


class OrderItem(models.Model):
    """購入履歴モデル"""
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Listing,on_delete=models.CASCADE,related_name='orderItems')
    ordered=models.BooleanField(default=False)
    quantity=models.IntegerField(default=1)


    def get_total_item_price(self):
        return self.quantity * self.item.listing_price


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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    stripe_charge_id = models.CharField(max_length=50)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

