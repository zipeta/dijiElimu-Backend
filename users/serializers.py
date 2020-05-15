from rest_framework import serializers
from allauth.account.adapter import get_adapter
from rest_framework.authtoken.models import Token
from rest_auth.registration.serializers import RegisterSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email',
            'phone_number', 'is_student', 'is_tutor', 'last_login',
            'created_at', 'is_active'
        )


class UserRegisterSerializer(RegisterSerializer):
    """serializer for UserRegisterSerializer."""
    first_name = serializers.CharField(max_length=100)
    second_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField()
    created_at = serializers.DateField()
    is_student = serializers.BooleanField()
    is_tutor = serializers.BooleanField()

    class Meta:
        model = User
        fields = '__all__'

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'is_student': self.validated_data.get('is_student', ''),
            'is_tutor': self.validated_data.get('is_tutor', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.set_password(self.cleaned_data['password'])
        user.save()
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):
    """docstriustomTokenSerializer."""
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user',)

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.data
        ).data
        is_student = serializer_data.get('is_student')
        is_tutor = serializer_data.get('is_tutor')
        return {
            'is_student': is_student,
            'is_tutor': is_tutor
        }
