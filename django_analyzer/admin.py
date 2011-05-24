from django.contrib import admin
from django_analyzer.models import *

class AnalyticsLogAdmin(admin.ModelAdmin):
    ordering = ('-timestamp',)
    list_display = ('user', 'ip', 'link', 'timestamp',)
    list_filter = ('user',)

admin.site.register(AnalyticsLog, AnalyticsLogAdmin)