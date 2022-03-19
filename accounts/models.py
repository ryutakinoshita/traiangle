from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from social_core.backends import username
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.staticfiles.storage import staticfiles_storage

class UserManager(BaseUserManager):
    """"基礎ユーザーモデル"""
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not  username:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            password=password,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email,password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


def user_portfolio_directory_path(instance, filename):
    return 'image-{0}/{1}'.format(instance.id, filename)

class GameType(models.Model):
    CHOICES = (
        ("10", "Apex"),
        ("20", "fortnite"),
        ("30", "valorant"),
        ("40", "COD"),
        ("50", "League of Legends"),
        ("60", "Overwatch"),
        ("70", "Minecraft"),
        ("80", "原神"),
        ("90", "遊戯王マスターデュエル"),
        ("100", "The Sandbox"),
        ("110", "Axie Infinity"),
        ("120", "Crypto Spells"),
        ("130", "Sorare"),
        ("140", "My Crypto Heroes"),
        ("150", "PolkaFantasy"),
        ("160", "CryptoKitties"),
    )


class User(AbstractBaseUser, PermissionsMixin):
    """"カスタムユーザーモデル"""
    user_name=models.CharField(max_length=30,blank=False,null=False)
    email = models.EmailField(max_length=100, unique=True)
    user_img = models.ImageField(upload_to='UserImg/',blank=True, null=True)
    certification = models.TextField(max_length=500, blank=True, null=True)
    game_type = models.CharField(max_length=100, choices=GameType.CHOICES, blank=True, null=True)
    privacy_user = models.BooleanField('プライバシー・ポリシーの確認',default=False)
    terms_user = models.BooleanField('利用規約への同意',default=False)
    created = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)



    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')



    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


    def get_absolute_url(self):
        return "/users/%i/" % self.pk

    def __str__(self):
            return self.email


