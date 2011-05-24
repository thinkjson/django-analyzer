from django import template
from django.db.models import Count
from django_analyzer.models import AnalyticsLog
from datetime import datetime, timedelta

register = template.Library()

@register.inclusion_tag('analyzer/list.html')
def most_active_users(number=10, days=30):
    month_ago = datetime.now() - timedelta(days=days)
    filtered_results = AnalyticsLog.objects.filter(timestamp__gte=month_ago).exclude(user=None)
    results = filtered_results.values_list('user__first_name', 'user__last_name').annotate(Count('id')).order_by('-id__count')[:number]
    return { 'results': results, 'fields': ['First', 'Last', 'Hits'] }

@register.inclusion_tag('analyzer/list.html')
def most_popular_urls(number=10, days=30):
    month_ago = datetime.now() - timedelta(days=days)
    filtered_results = AnalyticsLog.objects.filter(timestamp__gte=month_ago).exclude(user=None)
    results = filtered_results.values_list('uri').annotate(Count('id')).order_by('-id__count')[:number]
    return { 'results': results, 'fields': ['Url', 'Hits'] }

@register.inclusion_tag('analyzer/list.html')
def most_recent_hits(number=10, days=30):
    month_ago = datetime.now() - timedelta(days=days)
    filtered_results = AnalyticsLog.objects.filter(timestamp__gte=month_ago).exclude(user=None)
    results = filtered_results.values_list('user__first_name', 'user__last_name', 'ip', 'uri', 'timestamp').order_by('-timestamp')[:number]
    return { 'results': results, 'fields': ['First', 'Last', 'IP', 'Url', 'Timestamp'] }