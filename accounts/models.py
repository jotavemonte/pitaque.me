from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user_instance = User(
            email=email
        )
        user_instance.set_password(password or self.make_random_password())
        user_instance.save()
        return user_instance

    def create_superuser(self, email, password):
        user_instance = User(
            email=email,
            is_superuser=True,
            is_admin=True
        )
        user_instance.set_password(password)
        user_instance.save()
        return user_instance

    def create_admin(self, email, password):
        user_instance = User(
            email=email,
            is_admin=True
        )
        user_instance.set_password(password)
        user_instance.save()
        return user_instance


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    class Meta:
        ordering = ('email',)


class Contributor(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='contributor'
    )
    points = models.IntegerField(default=0)
    nickname = models.CharField(max_length=20)

    class Meta:
        ordering = ('nickname',)
