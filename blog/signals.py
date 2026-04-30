from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

from .models import Post
from history_tracker.models import Tracker
from history_tracker.get_request import current_request


@receiver(post_save, sender=Post)
def create_blog_post(sender, created, **kwargs):
    if created:
        print(f"{sender} created")
        Tracker.objects.create(
            user=User.objects.filter(username=current_request().user).first(),
            model=sender._meta.model.__name__,
            type_of_change="Created",
            changed=timezone.now()
        )


@receiver(post_save, sender=Post)
def save_blog_post(sender, **kwargs):
    print(f"{sender} saved")
    Tracker.objects.create(
        user=User.objects.filter(username=current_request().user).first(),
        model=sender._meta.model.__name__,
        type_of_change="Saved",
        changed=timezone.now()
    )


@receiver(post_delete, sender=Post)
def delete_blog_post(sender, **kwargs):
    print(f"{sender} deleted")
    Tracker.objects.create(
        user=User.objects.filter(username=current_request().user).first(),
        model=sender._meta.model.__name__,
        type_of_change="Deleted",
        changed=timezone.now()
    )
