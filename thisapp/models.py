from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone

from thisapp.manager import UserManager, _

# import the validators


class User(AbstractBaseUser, PermissionsMixin):
    """
    """
    # create instances of the validators

    email = models.EmailField(
        _("email address"),
        unique=True,
        max_length=255,
    )

    password = models.CharField(
        _("password"),
        max_length=255,
    )

    first_name = models.CharField(
        _("first name"),
        max_length=255
    )

    last_name = models.CharField(
        _("last name"),
        max_length=255
    )

    telephone = models.CharField(
        _("telephone"),
        max_length=255,
        default="",
    )

    date = models.DateTimeField(
        _("date"),
        default=timezone.now
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = "is_staff"

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["password"]

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    @property
    def is_staff(self):
        """ All admins are staff """
        return self.is_admin

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_full_name(self):
        """
        combines first name and last name, with a space between
        """
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        """ A short, informal identifier for the user such as their first name.  """
        return self.first_name


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
# https://testdriven.io/blog/django-custom-user-model/


# class User(AbstractUser):
#     """
#     full_name = is a composite of first_name and last_name
#     date = date_joined
#     """
#     email = models.EmailField(max_length=32, unique=True, )
#     password = models.CharField(max_length=255)
#     telephone = models.CharField(max_length=15, default='')
#     date = models.DateTimeField(default=timezone.now)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     REQUIRED_FIELDS = ["password"]
#     USERNAME_FIELD = "email"
#     EMAIL_FIELD = ""
#     date_joined = "date"

#     objects = User_manager()

#     def __str__(self):
#         return self.username
