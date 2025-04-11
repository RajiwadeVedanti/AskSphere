import logging
from rest_framework.status import HTTP_401_UNAUTHORIZED
from django.http import JsonResponse
from auth_user.models import CustomUser


class AuthMiddleware:
    def __init__(self, get_response):
        self.logger = logging.getLogger(__name__)
        self.get_response = get_response
        self.exclude_paths = ["/user", "/user/sign-up", "/user/get-login", "/user/login"]

    def __call__(self, request):
        try:
            path = request.path
            if any(path.startswith(ep) for ep in self.exclude_paths):
                return self.get_response(request)
            
            user_email = request.session.get("email")

            try:
                user = CustomUser.objects.get(email=user_email)
            except CustomUser.DoesNotExist:
                return JsonResponse({"error": "Authorization is missing or invalid."}, status=HTTP_401_UNAUTHORIZED)

            return self.get_response(request)
        except Exception as e:
            self.logger.exception(f"middleware exception: {(str(e))}")
            return self.get_response(request)
 