from django.contrib import admin
from .models import CasualtyReport

@admin.register(CasualtyReport)
class CasualtyReportAdmin(admin.ModelAdmin):
    list_display = ['victim_name', 'reporter', 'status', 'location', 'timestamp']
    list_filter = ['status', 'timestamp']
    search_fields = ['victim_name', 'reporter__username', 'location', 'condition']
    readonly_fields = ['timestamp']
    list_editable = ['status']
    
    fieldsets = (
        ('Report Information', {
            'fields': ('reporter', 'timestamp')
        }),
        ('Victim Details', {
            'fields': ('victim_name', 'contact_info', 'condition')
        }),
        ('Location & Status', {
            'fields': ('location', 'status')
        }),
    )
