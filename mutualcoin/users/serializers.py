from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'zip_code'
            'pin',
            'approved',
            'email',
            'is_staff',
            'is_superuser',
            'is_active',
            'phone',
            'first_name',
            'last_name',
            
        ]
        read_only_fields = (
            'id',
        )

        def update(self, instance, validated_data):
            instance.phone = validated_data.get('phone', instance.phone)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.username = validated_data.get('username', instance.username)
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


