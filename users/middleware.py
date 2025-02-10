from .models import UserActivityLog

class ActivityLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            activity = f'Visited {request.path}'
            UserActivityLog.objects.create(user=request.user, action=activity, path=request.path)
        response = self.get_response(request)
        return response