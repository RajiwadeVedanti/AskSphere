from rest_framework.serializers import Serializer, CharField
from ..models import CustomUser


class UserSignUpSerializer(Serializer):
    email = CharField(
        required=True,
        error_messages={'required': 'Email is required'}
    )
    first_name = CharField(
        required=True, max_length=30,
        error_messages={'required': 'First Name is required'}
    )
    last_name = CharField(
        required=True, max_length=30,
        error_messages={'required': 'Last Name is required'}
    )
    password = CharField(
        required=True, min_length=8, max_length=12,
        error_messages={
            'required': 'Password is required',
            'min_length': 'Ensure the password has at least 8 and atmost 12 characters.'     
        }
    )

    class Meta:
        model = CustomUser


class UserLoginSerializer(Serializer):
    email = CharField(
        required=True,
        error_messages={'required': 'Email is required'}
    )
    password = CharField(
        required=True, min_length=8, max_length=12,
        error_messages={
            'required': 'Password is required',
            'min_length': 'Ensure the password has at least 8 and atmost 12 characters.'          
        }
    )

    class Meta:
        model = CustomUser