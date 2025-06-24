from django.db import models
from django.conf import settings

# Create your models here.

class Service(models.Model):
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    availability_status = models.CharField(max_length=12, choices=AVAILABILITY_CHOICES, default='available')

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='service_requests')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='requests')
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.name} ({self.status})"

    class Meta:
        ordering = ['-timestamp']
