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
from .paginations import *
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from rest_framework.parsers import FileUploadParser, FormParser,MultiPartParser
# Create your views here.


class expAIViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `checkBody` action.
    """
    queryset = Softwarelibs.objects.all()
    serializer_class = SoftwareLibsSerializer
    
class DatasetsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `checkBody` action.
    """
    
    serializer_class = DatasetsSerializer
    permission_classes = [IsOwner | IsAdmin]
    def get_queryset(self):
        usr = self.request.user
        usr = User.objects.get(email=usr.email)
        if usr.roleid.rolename=="ADMIN":
            queryset=Datasets.objects.all()
        elif usr.roleid.rolename=="STUDENT":
            queryset = Datasets.objects.filter(datasettype=1)|Datasets.objects.filter(datasetowner = self.request.user) 
        else:
            usrclass= list(usr.usrclass.all()) 
            student = [list(i.user_set.all())  for i in usrclass]
            student = sum(student,[])
            queryset = Datasets.objects.filter(datasettype=1)|Datasets.objects.filter(datasetowner__in = student) 

        return queryset
    def perform_create(self, serializer):
        serializer.save(datasetowner=self.request.user)
    
    

class AccountsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `checkBody` action.
    """
    # permission_classes = (IsAdmin,)
    queryset = User.objects.all()
    pagination_class = LargeResultsSetPagination
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'name']
    
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
    @swagger_auto_schema(tags=['Đăng nhập - Đăng ký'])
    def post(self, serializer):
        serializer = LoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(self.request, user)
        return response.Response(UserSerializer(user).data)


class LogoutView(views.APIView):
    @swagger_auto_schema(tags=['Đăng nhập - Đăng ký'])
    def post(self, request):
        logout(request)
        return response.Response()
@method_decorator(name="post", decorator=swagger_auto_schema(tags=["Đăng nhập - Đăng ký"]))
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(tags=['Đăng nhập - Đăng ký'])
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
        @swagger_auto_schema(tags=['Đăng nhập - Đăng ký'])
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
                self.object.usrclass.set(serializer.data.get("usrclass"))
                self.object.usrdob=serializer.data.get("usrdob")
                self.object.usrfullname=serializer.data.get("usrfullname")
                self.object.usrfaculty=serializer.data.get("usrfaculty")

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

    @swagger_auto_schema(method='get',manual_parameters=[],responses={404: 'Not found', 200:'ok', 201:ExperimentsSerializer})
    @action(methods=['GET'], detail=False, url_path='get-list-exps')
    def get_list_exps(self, request):

        """
        lay ds bai thi nghiem theo id user
        """
        
        user = request.user
        user = User.objects.get( id = user.pk)


        epxs = Experiments.objects.filter(expcreatorid = user.id)
        return Response({"result": epxs})

    id_softlib = openapi.Parameter('id_softlib',openapi.IN_QUERY,description='id cua softlib',type=openapi.TYPE_NUMBER)
    @swagger_auto_schema(method='get',manual_parameters=[id_softlib],responses={404: 'Not found', 200:'ok', 201:ExperimentsSerializer})
    @action(methods=['GET'], detail=False, url_path='get-list-models')
    def get_list_models(self, request):

        """
        lay ds model theo id softlib
        """

        id_softlib = request.query_params.get('id_softlib')

        models = Models.objects.filter(modelsoftlibid = id_softlib)
        return Response({"result": models})

    #id_softlib = openapi.Parameter('id_softlib',openapi.IN_QUERY,description='id cua softlib',type=openapi.TYPE_NUMBER)
    @swagger_auto_schema(method='get',manual_parameters=[id_softlib],responses={404: 'Not found', 200:'ok', 201:ExperimentsSerializer})
    @action(methods=['GET'], detail=False, url_path='get-list-models')
    def get_list_datasets(self, request):
        usr = self.request.user
        usr = User.objects.get(email=usr.email)

        id_softlib = request.query_params.get('id_softlib')

        if usr.roleid.rolename=="ADMIN":
            queryset=Datasets.objects.all()
        elif usr.roleid.rolename=="STUDENT":
            queryset = Datasets.objects.filter(datasettype=1,expsoftwarelibid__pk = id_softlib)|Datasets.objects.filter(datasetowner = self.request.user,expsoftwarelibid__pk = id_softlib) 
        else:#giao vien
            usrclass= list(usr.usrclass.all()) 
            student = [list(i.user_set.all())  for i in usrclass]
            student = sum(student,[])
            queryset = Datasets.objects.filter(datasettype=1,expsoftwarelibid__pk = id_softlib)|Datasets.objects.filter(datasetowner__in = student,expsoftwarelibid__pk = id_softlib) 

        return queryset

    #start - stop train 
    id_exp = openapi.Parameter('id_exp',openapi.IN_QUERY,description='id cua exp',type=openapi.TYPE_NUMBER)
    paramsconfigs_json = openapi.Parameter('paramsconfigs_json',openapi.IN_QUERY,description='json string paramsconfig',type=openapi.TYPE_STRING)
    id_paramsconfigs = openapi.Parameter('paramsconfig_json',openapi.IN_QUERY,description='json string paramsconfig',type=openapi.TYPE_STRING)

    @swagger_auto_schema(method='get',manual_parameters=[id_exp, paramsconfigs_json],responses={404: 'Not found', 200:'ok', 201:ExperimentsSerializer})
    @action(methods=['GET'], detail=False, url_path='start-train')
    def start_train(self, request):

        """
        start train
        """
        
        user = request.user
        user = User.objects.get( id = user.pk)

        id_exp = request.query_params.get('id_exp')
        paramsconfigs_json = request.query_params.get('paramsconfigs_json')

        exp = Experiments.objects.filter(expid = id_exp)
        paramsconfigs = Paramsconfigs(jsonstringparams=paramsconfigs_json,trainningstatus=1)
        paramsconfigs.save()

        response = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'message': 'Start tranning',
            'data': paramsconfigs
        }

        return response

    
    
    
    @swagger_auto_schema(method='get',manual_parameters=[id_exp, id_paramsconfigs],responses={404: 'Not found', 200:'ok', 201:ExperimentsSerializer})
    @action(methods=['GET'], detail=False, url_path='stop-train')
    def stop_train(self, request):

        """
        stop train
        """
        
        user = request.user
        user = User.objects.get( id = user.pk)

        id_exp = request.query_params.get('id_exp')
        id_paramsconfigs = request.query_params.get('id_paramsconfigs')

        exp = Experiments.objects.filter(expid = id_exp)
        paramsconfigs = Paramsconfigs.objects.get(configid = id_paramsconfigs)



        response = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'message': 'Stop tranning',
            'data': []
        }

        return response
    
import zipfile
import uuid
import os
class DatasetsUploadView(views.APIView):
    parser_classes = [FormParser,MultiPartParser]

    def post(self, request):
        file_obj = request.data['file']
        new_name = uuid.uuid4()
        
        with zipfile.ZipFile(file_obj, mode='r', allowZip64=True) as file:
            
            directory_to_extract = f"datasets/{new_name}"
            file.extractall(directory_to_extract)

        response = {
                    'status': 'success',
                    'code': status.HTTP_201_CREATED,
                    'message': 'Data uploaded successfully',
                    'data': new_name
                }
        return Response(response)
