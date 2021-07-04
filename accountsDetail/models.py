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
        ("7", "その他の専門料理店"),
        ("9", "そば・うどん店"),
        ("10", "酒場、ビヤホール"),
        ("11", "バー、キャバレー、ナイトクラブ"),
        ("12", "喫茶店"),
        ("13", "その他の飲食店"),
        ("14", "ハンバーガー店"),
        ("15", "お好み焼・焼きそば・たこ焼店"),
        ("16", "分類されない飲食店"),
    )

class Restaurant(models.Model):
    """飲食店"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=8,blank=False,null=False)
    prefectures=models.CharField(max_length=40,blank=False,null=False)
    city=models.CharField(max_length=40,blank=False,null=False)
    address1=models.CharField(max_length=40,blank=False,null=False)
    address2=models.CharField(max_length=40,blank=True)
    restaurant_img1 = models.ImageField(upload_to='restaurantImg/',blank=False,null=False)
    restaurant_img2 = models.ImageField(upload_to='restaurantImg/',blank=False,null=False)
    restaurant_img3= models.ImageField(upload_to='restaurantImg/',blank=False,null=False)
    restaurant_type = models.CharField(max_length=100, choices=TypeSub.Types,blank=False,null=False)
    restaurant_name=models.CharField(max_length=40,blank=False,null=False)
    certification = models.TextField(max_length=500, blank=True, null=True)

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