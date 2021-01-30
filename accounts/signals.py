from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

from .models import Usuario


def user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name="usuario")
        instance.groups.add(group)

        Usuario.objects.create(
            user=instance,
            name=instance.username
        )


post_save.connect(user_profile, sender=User)
