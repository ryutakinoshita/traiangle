from django.db import models
from django.utils import timezone
from accounts.models import User



Time= (
    ("1", "10分以内"),
    ("2", "10分"),
    ("3", "20分"),
    ("4", "30分"),
    ("5", "40分"),
    ("6", "50分"),
    ("7", "60分"),
    ("8", "60分以上"),
)

class Recipe(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    recipe_img1= models.ImageField(upload_to='listingImg',blank=False, null=False)
    recipe_img2= models.ImageField(upload_to='listingImg',blank=True, null=True)
    recipe_img3= models.ImageField(upload_to='listingImg',blank=True, null=True)
    recipe_title= models.CharField(max_length=100, blank=False, null=False)
    recipe_text= models.TextField(max_length=2000, blank=False, null=False)
    recipe_time=models.CharField(max_length=100,choices=Time, blank=False, null=False)
    food_tag=models.CharField(max_length=100,blank=False, null=False)
    add_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
            return str(self.user)