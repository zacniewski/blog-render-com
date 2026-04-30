from django.db import models
from django.utils import timezone


class Tracker(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    model = models.CharField(max_length=200)
    type_of_change = models.TextField()
    changed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.type_of_change} {self.model} by {self.user} at {self.changed}"
