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



class Withdrawals(models.Model):
    CHOICES = (
        ("10","月額料金が高い"),
        ("20","使用のメリットをあまり感じられなかった"),
        ("30","使用していない為"),
        ("40","他アプリへの乗り換え"),
        ("50","その他"),
    )


class Withdrawal(models.Model):
    withdrawal_user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact_us=models.CharField(max_length=20,choices=Withdrawals.CHOICES,blank=False,null=False)
    message=models.TextField(max_length=1000,blank=False,null=False)

    def __str__(self):
        return self.message


class Contacts(models.Model):
    CHOICES =(
        ("10","商品について"),
        ("20","返品・返金要請"),
        ("30","迷惑行為"),
        ("40","違法商品の販売"),
        ("50","その他"),
    )


class Contact(models.Model):
    contact_user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact_us=models.CharField(max_length=20,choices=Contacts.CHOICES,blank=False,null=False)
    message=models.TextField(max_length=1000,blank=False,null=False)

    def __str__(self):
        return self.message

class Games(models.Model):
    CHOICES =(
        ("10","Apex"),
        ("20","fortnite"),
        ("30","valorant"),
        ("40","COD"),
        ("50","League of Legends"),
        ("60","Overwatch"),
        ("70","Minecraft"),
        ("80","原神"),
        ("90","遊戯王マスターデュエル"),
        ("100","The Sandbox"),
        ("110","Axie Infinity"),
        ("120","Crypto Spells"),
        ("130","Sorare"),
        ("140","My Crypto Heroes"),
        ("150","PolkaFantasy"),
        ("160","CryptoKitties"),
    )


class GameForm(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    games=models.CharField(max_length=20,choices=Games.CHOICES,blank=False,null=False)

    def __str__(self):
        return self.games


