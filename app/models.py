from django.db import models
from accounts.models import User


class StripeCustomer(models.Model):
    """サブスクリプションモデル"""
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


CHOICES =(
    ("10","アプリの不具合"),
    ("20","スパムと迷惑行為について"),
    ("30","要注意コンテンツ"),
    ("40","サービスの改善について"),
    ("50","商品の報告"),
    ("60","その他"),
    ("70","退会"),
)


class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact_us=models.CharField(max_length=20,choices=CHOICES)
    email=models.EmailField(max_length=100,null=False, blank=True)
    message=models.TextField(max_length=1000,null=False, blank=True)

    def __str__(self):
        return self.message
