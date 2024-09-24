from django.db import models


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

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
