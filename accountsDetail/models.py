from django.db import models
from accounts.models import User
from listing.models import Listing
from django.utils import timezone



class TypeSub(models.Model):
    Types=(
        ("1", "食堂，レストラン"),
        ("2", "日本料理店"),
        ("3", "料亭"),
        ("4", "中華料理店"),
        ("5", "ラーメン店"),
        ("6", "焼肉店"),
        ("7", "そば・うどん店"),
        ("8", "酒場、ビヤホール"),
        ("9", "喫茶店"),
        ("10", "その他の飲食店"),
        ("11", "ハンバーガー店"),
        ("12", "イタリア料理店"),
        ("13", "アジア料理店"),

    )

class Hour(models.Model):
    Types=(
        ("1", "営業時間内の受け取り"),
        ("2", "営業時間後30分以内であれば可"),
        ("3", "営業時間後60分以内であれば可"),
        ("4", "TELでのお問い合わせ確認"),
    )

class Restaurant(models.Model):
    """飲食店"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_name=models.CharField(max_length=40,blank=False,null=False)
    restaurant_img1 = models.ImageField(upload_to='restaurantImg/',blank=False,null=False)
    restaurant_img2 = models.ImageField(upload_to='restaurantImg/',blank=False,null=False)
    restaurant_img3= models.ImageField(upload_to='restaurantImg/',blank=False,null=False)
    restaurant_type = models.CharField(max_length=100, choices=TypeSub.Types,blank=False,null=False)
    zip_code = models.CharField(max_length=8,blank=False,null=False)
    prefectures=models.CharField(max_length=40,blank=False,null=False)
    city=models.CharField(max_length=40,blank=False,null=False)
    address1=models.CharField(max_length=40,blank=False,null=False)
    address2=models.CharField(max_length=40,blank=True)
    certification = models.TextField(max_length=500, blank=True, null=True)
    nearest_station=models.CharField(max_length=40,blank=True)
    business_hours_start=models.CharField(max_length=40,blank=True,null=True)
    business_hours_end=models.CharField(max_length=40,blank=True,null=True)
    business_hours_option=models.CharField(max_length=40, choices=Hour.Types,blank=False,null=False)


    def __str__(self):
            return self.restaurant_name




class Review(models.Model):
    """レビューモデル"""
    target=models.ForeignKey(Listing,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.SET_DEFAULT,default='退会済みのユーザー')
    answer_text=models.TextField(max_length=300,blank=True,null=True)
    time=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.answer_text