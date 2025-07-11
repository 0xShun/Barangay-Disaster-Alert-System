from django.db import models
from django.conf import settings
from django.utils import timezone

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
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

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

class EmergencyHotline(models.Model):
    """
    Emergency hotline directory for various agencies and services.
    """
    agency_name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    description = models.TextField()
    category = models.CharField(max_length=50, default='General')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.agency_name} - {self.number}"

    class Meta:
        ordering = ['category', 'agency_name']

class ServiceRequirement(models.Model):
    service = models.ForeignKey(Service, related_name='service_requirements', on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    requirement_type = models.CharField(max_length=10, choices=[('text', 'Text'), ('file', 'File'), ('photo', 'Photo')])

    def __str__(self):
        return f"{self.label} ({self.get_requirement_type_display()})"

class ServiceRequestRequirementUpload(models.Model):
    request = models.ForeignKey('ServiceRequest', related_name='uploads', on_delete=models.CASCADE)
    requirement = models.ForeignKey(ServiceRequirement, on_delete=models.CASCADE)
    file = models.FileField(upload_to='service_uploads/', blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.requirement.label} for {self.request}"
