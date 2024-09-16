from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


User = get_user_model()

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
    ]
    STATUS_CHOICES = [
        ('new', 'new'),
        ('in progress', 'in progress'),
        ('completed', 'completed')
    ]

    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("task_detail", args=[str(self.id)])

class Photo(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.image.name

    @property
    def image_url(self):
        return self.image.url


