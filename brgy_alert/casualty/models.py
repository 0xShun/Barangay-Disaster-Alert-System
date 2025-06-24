from django.db import models
from django.conf import settings

class CasualtyReport(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('resolved', 'Resolved'),
    ]
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='casualty_reports')
    victim_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    condition = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.victim_name} ({self.status})"

    class Meta:
        ordering = ['-timestamp']
