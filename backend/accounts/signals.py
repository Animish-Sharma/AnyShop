from .models import UserAccount
from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save,sender=UserAccount)
def post_save_create_user(sender,instance,created,**kwargs):
    if created:
        user= User.objects.create(first_name = instance.first_name,last_name = instance.last_name,email=instance.email,username=instance.username)
        user.set_password(instance.password)
        user.save()
        instance.password = user.password
        instance.save()


@receiver(post_delete,sender=UserAccount)
def post_delete_user(sender, instance, using, **kwargs):
    user = User.objects.get(username=instance.username)
    user.delete()