from django.contrib import admin
from .models import CasualtyReport

@admin.register(CasualtyReport)
class CasualtyReportAdmin(admin.ModelAdmin):
    list_display = ('victim_name', 'reporter', 'condition', 'location', 'status', 'timestamp')
    list_filter = ('status', 'condition', 'location')
    search_fields = ('victim_name', 'reporter__username', 'location', 'condition')
    ordering = ('-timestamp',)
