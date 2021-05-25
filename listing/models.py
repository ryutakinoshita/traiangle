from django.db import models
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
    listing_img1= models.ImageField(upload_to='listingImg/')
    listing_img2= models.ImageField(upload_to='listingImg/')
    listing_img3= models.ImageField(upload_to='listingImg/')
    listing_type =models.CharField(max_length=100, choices=Type.TypeListing, blank=True, null=False)
    listing_name=models.CharField(max_length=100,blank=True, null=False)
    listing_text=models.TextField(max_length=500,blank=True, null=True)
    listing_price=models.IntegerField(blank=True, null=True)


    def __str__(self):
            return self.listing_name

# class BuyingHistory(models.Model):
#     buying_history= models.ForeignKey(Listing,on_delete=models.PROTECT)
#     buying_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
#     is_sended = models.BooleanField(default=False)
#     stripe_id = models.CharField(max_length=200)
#     created_at = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return '{} {} {}'.format(self.Listing, self.user.email, self.is_sended)