from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User

def user_create_reciever(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance,
            name = instance.username,
            email = instance.email,
        )


post_save.connect(user_create_reciever,sender=User)
