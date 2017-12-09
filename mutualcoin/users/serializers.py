from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.registration.views import RegisterView

User = get_user_model()



class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)  
    phone = serializers.CharField(required=True, write_only=True)
    zip_code = serializers.CharField(required=True, write_only=True)
    pin = serializers.CharField(required=True, write_only=True, min_length=4)

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'zip_code' : self.validated_data.get('zip_code', ''),
            'pin' : self.validated_data.get('pin', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'zip_code',
            'pin',
            'approved',
            'email',
            'is_staff',
            'is_superuser',
            'is_active',
            'phone',
            'first_name',
            'last_name',
            'date_joined', 
            'last_login'            
        ]

        read_only_fields = (
            'id',
        )

        def update(self, instance, validated_data):
            instance.phone = validated_data.get('phone', instance.phone)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.save()
            return instance
        #
        # def get_user_sell_orders(request):
        #     return SellOrder.objects.filter(user=request.data['user'])


class UserDetailsSerializer(ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'last_login', 'is_staff', 'is_superuser')
        read_only_fields = ('email', )


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()



    


