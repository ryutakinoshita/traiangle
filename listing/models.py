from django.db import models
from autoslug import AutoSlugField
from accounts.models import User
from django.utils import timezone

class Type(models.Model):
    TypeListing=(
        ("1", "和食"),
        ("2", "中華料理"),
        ("3", "韓国料理"),
        ("4", "アジア料理"),
        ("5", "フランス料理"),
        ("6", "イタリア料理"),
        ("7", "肉メインの料理"),
        ("8", "魚メインの料理"),
        ("9", "野菜メインの料理"),
        ("10", "揚げ物"),
        ("11", "ファストフード"),
        ("12", "ヘルシー料理"),
        ("13", "丼"),
        ("14", "ベーカリー"),
        ("15", "スイーツ"),
        ("16", "その他"),
    )

class Hour(models.Model):
    Hours=(
        ("1", "本日中の召し上がり"),
        ("2", "明日までに召し上がり"),
        ("3", "3-5日以内の召し上がり"),
        ("4", "7日以内の召し上がり"),
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
    listing_originally_price=models.IntegerField(blank=True, null=True)
    listing_price=models.IntegerField(blank=True, null=True)
    consumption_time=models.CharField(max_length=40, choices=Hour.Hours,blank=False,null=False)
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
    order_date=models.DateTimeField(default=timezone.now)
    confirmed = models.ManyToManyField(User, related_name='confirmed_listing', blank=True)


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

