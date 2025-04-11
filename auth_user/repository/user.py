import logging
from django.shortcuts import redirect, render
from ..models import CustomUser
from django.contrib.auth import authenticate


logger = logging.getLogger(__name__)

class UserRepository:
    def user_sign_up(self, request, request_data):
        try:
            try:
                _ = CustomUser.objects.get(email=request_data.get("email"))
            except CustomUser.DoesNotExist:                        
                user = CustomUser.objects.create(
                    **request_data
                )
                user.set_password(request_data["password"])
                user.save()

                return redirect("/user/get-login")
        
            return render(request, 'sign_up.html', {'errors': "User is already signed up!"})

        except Exception as e:
            logger.exception(f"user_sign_up exception: {str(e)}")
            return render(request, 'sign_up.html', {'errors': "Unexpected error occured!"})
        

    def user_login(self, request):
        try:
            request_data = request.data
            auth_user = authenticate(
                username=request_data.get("email"),
                password=request_data.get("password")
            )
            if auth_user:
                request.session["user_id"] = auth_user.id
                request.session["email"] = auth_user.email

                return redirect("/qa/get-question")
            return render(request, 'login.html', {'errors': "Invalid credentials"})
        except Exception as e:
            logger.exception(f"user_login exception: {str(e)}")
            return render(request, 'login.html', {'errors': "Unexpected error occured!"})
        

    def user_logout(self, request):
        try:
            del request.session["user_id"]
            del request.session["email"]

            return redirect("/user/get-login")
        except Exception as e:
            logger.exception(f"user_logout exception: {str(e)}")
            return redirect("/user/get-login")