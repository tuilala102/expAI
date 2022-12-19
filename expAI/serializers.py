from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth import authenticate
from rest_framework import serializers
from .validators import validate_username
from .permissions import *

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
class ChangeNameSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    password = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    # usrclass = serializers.ListField(required=True)
    usrfullname = serializers.CharField(required=True)
    usrdob = serializers.DateField(required=True)
    usrfaculty = serializers.CharField(required=True)
class DestroyUserSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    password = serializers.CharField(required=True)

class ChangePassword2Serializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    id_user = serializers.CharField(required=True)
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

            'usrfullname',
            'usrdob',
            'usrfaculty'
        )
        read_only_fields = ( 'is_staff','last_login', 'is_active', 'joined_at')
        extra_kwargs = {
            'password': {'required': True, 'write_only': True},
            'name': {'required': True}
        }

    # @staticmethod
    # def validate_email(value):
    #     return validate_username(value)

    def create(self, validated_data):
        return User.objects.create_user(
                    validated_data.pop('email'),
                    validated_data.pop('password'),
                    **validated_data
                )

class SoftwareLibsSerializer(ModelSerializer):
    class Meta:
        model = Softwarelibs
        fields = '__all__'


class ExperimentsSerializer(ModelSerializer):
    class Meta:
        model = Experiments
        fields = '__all__'
        read_only_fields = ('expcreatorid',)


class DatasetsSerializer(ModelSerializer):
    class Meta:
        model = Datasets
        fields = '__all__'
        read_only_fields = ('datasetowner',"datasetcreatedtime",)

class ResultsSerializer(ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'
        read_only_fields = ('resultaccuracy','resultdetail',)
class ModelsSerializer(ModelSerializer):
    class Meta:
        model = Models
        fields = '__all__'

class ParamsconfigsSerializer(ModelSerializer):
    class Meta:
        model = Paramsconfigs
        fields = '__all__'


class ModelsSerializer(ModelSerializer):
    class Meta:
        model = Models
        fields = ["modelid","modelname","modeltype","expsoftwarelibid","modelfiletutorial","modelfiledescription",
        "modeldescription","modeleventtype","modelcreator","modelcreatedtime",'modelowner']
        read_only_fields = ('modelowner',)
        

class TrainningresultsSerializer(ModelSerializer):
    class Meta:
        model = Trainningresults
        fields = '__all__'