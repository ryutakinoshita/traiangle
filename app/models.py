from django.db import models
from accounts.models import User
from phonenumber_field.modelfields import PhoneNumberField

class StripeCustomer(models.Model):
    """サブスクリプションモデル"""
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


CHOICES =(
    ("10","月額料金が高い"),
    ("20","使用のメリットをあまり感じられなかった"),
    ("30","使用していない為"),
    ("40","他アプリへの乗り換え"),
    ("50","その他"),
)


class Withdrawal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact_us=models.CharField(max_length=20,choices=CHOICES,blank=False,null=False)
    message=models.TextField(max_length=1000,blank=False,null=False)

    def __str__(self):
        return self.message



Contacts =(
    ("10","商品について"),
    ("20","返品・返金要請"),
    ("30","迷惑行為"),
    ("40","違法商品の販売"),
    ("50","その他"),
)


class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact_us=models.CharField(max_length=20,choices=Contacts,blank=False,null=False)
    message=models.TextField(max_length=1000,blank=False,null=False)

    def __str__(self):
        return self.message

