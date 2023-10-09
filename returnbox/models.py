from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile

# Create your models here.

class BoxReturn(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='box_returns')
    number_of_boxes_returned = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"User: {self.user.user.username}, Status: {self.status}"
