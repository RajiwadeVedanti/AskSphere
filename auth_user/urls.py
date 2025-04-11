from django.urls import path
from .views import UserSignUp, UserLogin, UserLogout

urlpatterns = [
    path("", UserSignUp.as_view(), name='create_user_account'),
    path("sign-up", UserSignUp.as_view(), name='user_sign_up'),
    path("get-login", UserLogin.as_view(), name='get_login_page'),
    path("login", UserLogin.as_view(), name='user_login'),
    path("logout", UserLogout.as_view(), name='user_logout')
]