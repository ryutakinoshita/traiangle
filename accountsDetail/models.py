from django.db import models
from accounts.models import User


class Type(models.Model):
    Types=(
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


class Producer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=8,blank=True)
    prefectures_city=models.CharField(max_length=40,blank=True)
    producer_img = models.ImageField(upload_to='producerImg/')
    producer_name=models.CharField(max_length=40,blank=True)
    producer_type = models.CharField(max_length=100, choices=Type.Types, blank=True, null=False)
    certification = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        permissions = (
            ('view_content', 'View content'),
        )

    def __str__(self):
            return self.producer_name


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=8,blank=True)
    prefectures=models.CharField(max_length=40,blank=True)
    city=models.CharField(max_length=40,blank=True)
    address1=models.CharField(max_length=40,blank=True)
    address2=models.CharField(max_length=40,blank=True)
    restaurant_img = models.ImageField(upload_to='restaurantImg/')
    restaurant_type = models.CharField(max_length=100, choices=TypeSub.Types, blank=True, null=False)
    restaurant_name=models.CharField(max_length=40,blank=True)
    certification = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
            return self.restaurant_name

class RestaurantImage(models.Model):
    user = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image_name1=models.CharField(max_length=40,blank=True)
    restaurant_img1= models.ImageField(upload_to='restaurantImg/')
    image_name2=models.CharField(max_length=40,blank=True)
    restaurant_img2= models.ImageField(upload_to='restaurantImg/')
    image_name3=models.CharField(max_length=40,blank=True)
    restaurant_img3= models.ImageField(upload_to='restaurantImg/')

    def __str__(self):
            return self.restaurant_img1.url


