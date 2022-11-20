from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth import authenticate
from rest_framework import serializers
from .validators import validate_username


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'last_login',
            'email',
            'name',
            'is_active',
            'joined_at',
            'password',
            'is_staff',
        )
        read_only_fields = ('last_login', 'is_active', 'joined_at')
        extra_kwargs = {
            'password': {'required': True, 'write_only': True},
            'name': {'required': True}
        }

    @staticmethod
    def validate_email(value):
        return validate_username(value)

    def create(self, validated_data):
        return User.objects.create_user(
                    validated_data.pop('email'),
                    validated_data.pop('password'),
                    **validated_data
                )

class SoftwareLibsSerializer(ModelSerializer):
    class Meta:
    #         softwarelibid = models.CharField(db_column='softwarelibID', primary_key=True, max_length=20)  # Field name made lowercase.
    # softwarelibname = models.CharField(db_column='softwarelibName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # softwareliburl = models.CharField(db_column='softwarelibURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    # softwarelibdescription = models.CharField(db_column='softwarelibDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.

        model = Softwarelibs
        fields = ["softwarelibid","softwarelibname","softwareliburl","softwarelibdescription"]


