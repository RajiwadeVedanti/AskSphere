from django.shortcuts import render
from rest_framework.views import APIView
from .repository.user import UserRepository
from .serializers.user import UserSignUpSerializer, UserLoginSerializer

class UserSignUp(APIView):
    def get(self, request):
        return render(request, 'sign_up.html')

    def post(self, request):
        request_data = UserSignUpSerializer(data=request.data)
        if not request_data.is_valid():
            error_key = list(request_data.errors.keys())[0]
            error_msg = request_data.errors[error_key][0]
            return render(request, 'sign_up.html', {'errors': error_msg})

        result = UserRepository().user_sign_up(request, request_data.data)

        return result
    
class UserLogin(APIView):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        request_data = UserLoginSerializer(data=request.data)
        if not request_data.is_valid():
            error_key = list(request_data.errors.keys())[0]
            error_msg = request_data.errors[error_key][0]
            return render(request, 'login.html', {'errors': error_msg})

        result = UserRepository().user_login(request)
        return result

class UserLogout(APIView):
    def post(self, request):
        result = UserRepository().user_logout(request)
        return result
    