from rest_framework import viewsets, status
from .models import *
from .serializers import *
from rest_framework import views, generics, response, permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth import login, logout
from django.conf import settings
from rest_framework.permissions import IsAuthenticated   
from .permissions import *
# Create your views here.


class expAIViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `checkBody` action.
    """
    queryset = Softwarelibs.objects.all()
    serializer_class = SoftwareLibsSerializer

class AccountsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `checkBody` action.
    """
    permission_classes = (IsAdmin,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
class ChangeUserPasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePassword2Serializer
    def get_object(self, queryset=None):
            id_user = self.request.data.get('id_user')
            obj = self.queryset.get(id=id_user)
            return obj
    def update(self, request):
        """
        Change User's Password API
        """
        obj = self.get_object()
        new_password = request.data.get('new_password')
        obj.set_password(new_password)
        obj.save()
        return Response({"result": "Success"})

class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, serializer):
        serializer = LoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(self.request, user)
        return response.Response(UserSerializer(user).data)


class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return response.Response()


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        login(self.request, user)


class ChangePasswordView(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteUserView(generics.UpdateAPIView):
        """
        An endpoint for changing name.
        """
        serializer_class = DestroyUserSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            obj = User.objects.get( id = obj.pk)
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check password
                if not self.object.check_password(serializer.data.get("password")):
                    return Response({"password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                
                self.object.delete()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'User destroy successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ChangeNameView(generics.UpdateAPIView):
        """
        An endpoint for changing name.
        """
        serializer_class = ChangeNameSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            obj = User.objects.get( id = obj.pk)
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check password
                if not self.object.check_password(serializer.data.get("password")):
                    return Response({"password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.name=serializer.data.get("name")
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Name updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get_object(self, *args, **kwargs):
        return self.request.user
    # # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    # #                       IsOwnerOrReadOnly]
    # test_param1 = openapi.Parameter('check_type', openapi.IN_QUERY, description="height or width", type=openapi.TYPE_STRING)
    # test_param2 = openapi.Parameter('id', openapi.IN_QUERY, description="id of expAI", type=openapi.TYPE_NUMBER)
    # user_response = openapi.Response('response description', StudientSerializer)

    # @swagger_auto_schema(method='get', manual_parameters=[test_param1, test_param2], responses={404: 'Not found', 200:'ok', 201:StudientSerializer})
    # @action(methods=['GET'], detail=False, url_path='check-body')
    # def check_body(self, request):
    #     """
    #     Check body API
    #     """
    #     check_type = request.query_params.get('check_type')
    #     id = request.query_params.get('id')

    #     print(check_type, id)
    #     obj = self.queryset.get(id=id)
    #     rs = ""
    #     if check_type == 'height':
    #         if obj.height > 1:
    #             rs = "tall"
    #         else:
    #             rs = "short"
    #     else:
    #         if obj.weight > 1:
    #             rs = "fat"
    #         else:
    #             rs = "thin"
    #     return Response({"result": rs})

    # @action(methods=['POST'], detail=False)
    # def echo(self, request):
    #     # deserializer
    #     obj = StudientSerializer(request.data)
    #     print(obj)
    #     # serializer
    #     return Response(obj.data)

    # @action(methods=['GET'], detail=False)
    # def find_by_name(self, request):
    #     name = request.query_params.get('name')
    #     print(self.queryset)
    #     objs = expAI.objects.filter(name__exact=name)
    #     return Response(StudientSerializer(objs).data)

class ExperimentsViewSet(viewsets.ModelViewSet):
    queryset = Experiments.objects.all()
    serializer_class = ExperimentsSerializer

    param1 = openapi.Parameter('id_model',openapi.IN_QUERY,description='id cua model',type=openapi.TYPE_NUMBER)
    @swagger_auto_schema(method='get',manual_parameters=[param1],responses={404: 'Not found', 200:'ok', 201:ExperimentsSerializer})
    @action(methods=['GET'], detail=False, url_path='get-models-name')
    def get_model_name(self, request):
        """
        get model name API
        """
        id_model = request.query_params.get('id_model')

        obj = Models.objects.get(modelid = id_model)
        return Response({"result": obj.modelname})