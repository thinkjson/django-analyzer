from django.db import models
from django.contrib.auth.models import User

class AnalyticsLog(models.Model):
    """Logs each and every hit against the system for auditing purposes."""
    user = models.ForeignKey(User, null=True, blank=True)
    ip = models.IPAddressField()
    uri = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.uri

    def link(self):
        return "<a href='%s'>%s</a>" % (self.uri, self.uri)
    link.allow_tags = True