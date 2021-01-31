from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.dispatch import receiver

from .models import Usuario


def user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name="usuarios")
        instance.groups.add(group)

        Usuario.objects.create(
            user=instance,
            name=instance.username
        )
        print("Profile created")


post_save.connect(user_profile, sender=User)


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    print("User logged in")


@receiver(user_login_failed)
def log_user_login_failed(sender, request, user, **kwargs):
    print("User failed to log in.")


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    print("User logged out")
