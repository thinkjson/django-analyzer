from django_analyzer.models import AnalyticsLog

class ViewAnalyticsMiddleware(object):
    """
    Keeps track of application usage based on views.
    """
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_anonymous():
            user = None
        else:
            user = request.user

        full_path = request.get_full_path()[:255]
        
        log = AnalyticsLog(user=user, uri=full_path, ip=request.META['REMOTE_ADDR'])
        log.save()