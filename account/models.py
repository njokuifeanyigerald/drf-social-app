from django.db import models


from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, UserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

import uuid


class MyUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        if not name:
            raise ValueError("The given name must be set")
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        name = self.model.normalize_username(name)
        user = self.model(name=name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, name, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)


    def create_superuser(self, name, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Gender(models.TextChoices):
       Male = "Male"
       Female = "Female"
    
    class Country(models.TextChoices):
        Nigeria="Nigeria"
        Ghana ="Ghana"
        South_Africa ="South Africa"
        Tanzania ="Tanzania"
        Morocco ="Morocco"
        Algeria = "Algeria"
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        _("name"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        )
        
    )
    email = models.EmailField(_("email address"),blank=False, unique=True, help_text=_(
        "Email is required"
    ))
    avatar = models.ImageField(upload_to='avatars', blank=True,  null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    gender = models.CharField(max_length=100, choices=Gender.choices,blank=False)
    phone_number= models.CharField(max_length=25,blank=False, unique=True)
    country = models.CharField(max_length=100, choices=Country.choices,blank=False)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

   

    objects = MyUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "gender","phone_number", "country"]


    def get_full_name(self):
        return self.full_name

    def __str__(self):
        return self.email

