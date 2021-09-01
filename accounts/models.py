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


class Prefectures(models.Model):
    Types=(
        ("1", "三重県"),
        ("2", "滋賀県"),
        ("3", "京都府"),
        ("4", "大阪府"),
        ("5", "兵庫県"),
        ("6", "奈良県"),
        ("7", "和歌山県"),
    )

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

class Bank(models.Model):
    code=(
        ("0001", "みずほ銀行"),
        ("0005", "三菱UFJ銀行"),
        ("0009", "三井住友銀行"),
        ("0010", "りそな銀行"),
        ("0033", "PayPay銀行"),
        ("0034", "セブン銀行"),
        ("0035", "ソニー銀行"),
        ("0036", "楽天銀行"),
        ("0038", "住信SBIネット銀行"),
        ("0039", "auじぶん銀行"),
        ("0040", "イオン銀行"),
        ("0042", "ローソン銀行"),
        ("0157", "滋賀銀行"),
        ("0158", "京都銀行"),
        ("0159", "関西みらい銀行"),

    )



class User(AbstractBaseUser, PermissionsMixin):
    """"カスタムユーザーモデル"""
    first_name=models.CharField(max_length=30,blank=False,null=False)
    last_name=models.CharField(max_length=30,blank=False,null=False)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=11, blank=False,null=False)
    zip_code = models.CharField(max_length=8,blank=True, null=True)
    prefectures = models.CharField(max_length=40,choices=Prefectures.Types,blank=True, null=True)
    city = models.CharField(max_length=40,blank=True, null=True)
    address1 = models.CharField(max_length=40,blank=True, null=True)
    address2 = models.CharField(max_length=40,blank=True, null=True)
    restaurant_img1 = models.ImageField(upload_to='restaurantImg/',blank=True, null=True)
    restaurant_img2 = models.ImageField(upload_to='restaurantImg/',blank=True, null=True)
    restaurant_img3= models.ImageField(upload_to='restaurantImg/',blank=True, null=True)
    rest_name= models.CharField(max_length=100,blank=True, null=True)
    restaurant_type = models.CharField(max_length=100, choices=TypeSub.Types,blank=True, null=True)
    certification = models.TextField(max_length=500, blank=True, null=True)
    nearest_station = models.CharField(max_length=40, blank=True, null=True)
    business_hours_start = models.CharField(max_length=40, blank=True, null=True)
    business_hours_end = models.CharField(max_length=40, blank=True, null=True)
    business_hours_option = models.CharField(max_length=40, choices=Hour.Types,blank=True, null=True)
    stripe_user_id = models.CharField(max_length=50)
    stripe_first_name_kana = models.CharField(max_length=30,blank=True, null=True)
    stripe_last_name_kana = models.CharField(max_length=30,blank=True, null=True)
    stripe_gender=models.CharField(max_length=100,blank=True, null=True)
    stripe_state = models.CharField(max_length=30,blank=True, null=True)
    stripe_city = models.CharField(max_length=100,blank=True, null=True)
    stripe_town = models.CharField(max_length=100,blank=True, null=True)
    stripe_line1 = models.CharField(max_length=100,blank=True, null=True)
    stripe_line2 = models.CharField(max_length=100,blank=True, null=True)
    stripe_postal_code = models.CharField(max_length=8,blank=True, null=True)
    stripe_state_kana = models.CharField(max_length=100,blank=True, null=True)
    stripe_city_kana = models.CharField(max_length=100,blank=True, null=True)
    stripe_town_kana = models.CharField(max_length=100,blank=True, null=True)
    stripe_line1_kana = models.CharField(max_length=100,blank=True, null=True)
    stripe_line2_kana = models.CharField(max_length=100,blank=True, null=True)
    stripe_day = models.CharField(max_length=2,blank=True, null=True)
    stripe_month = models.CharField(max_length=2,blank=True, null=True)
    stripe_year = models.CharField(max_length=4,blank=True, null=True)
    stripe_account_number=models.CharField(max_length=100,blank=True, null=True)
    stripe_bunk_code=models.CharField(max_length=100,choices=Bank.code,blank=True, null=True)
    stripe_routing_number=models.CharField(max_length=100,blank=True, null=True)
    stripe_account_holder_name=models.CharField(max_length=100,blank=True, null=True)
    stripe_img = models.ImageField(upload_to='stripeImg/', blank=True, null=True)
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


