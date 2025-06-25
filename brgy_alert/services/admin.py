from django.contrib import admin
from .models import Service, ServiceRequest, EmergencyHotline

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'availability_status', 'created_at']
    list_filter = ['availability_status']
    search_fields = ['name', 'description']

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'status', 'timestamp']
    list_filter = ['status', 'timestamp']
    search_fields = ['user__username', 'service__name', 'reason']
    readonly_fields = ['timestamp']

@admin.register(EmergencyHotline)
class EmergencyHotlineAdmin(admin.ModelAdmin):
    list_display = ['agency_name', 'number', 'category', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['agency_name', 'number', 'description']
    readonly_fields = ['created_at', 'updated_at']
