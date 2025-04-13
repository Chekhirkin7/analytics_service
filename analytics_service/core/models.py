from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    event_type = models.CharField(max_length=100)
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
    processed_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.event_type} by {self.user.username} at {self.timestamp}"
