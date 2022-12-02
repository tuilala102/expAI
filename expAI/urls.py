from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from expAI import views
from rest_framework import permissions
# from django.conf.urls import url


schema_view = get_schema_view(
    openapi.Info(
        title="expAI API docs",
        default_version='v0.1',
        description="Test API docs",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        #license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Create a router and register our viewsets with it.
router = DefaultRouter()


router.register(r'softwarelibs', views.SoftwarelibsViewSet)
router.register(r'accounts', views.AccountsViewSet)
router.register(r'experiment',views.ExperimentsViewSet)
router.register(r'models', views.ModelsViewSet)
router.register(r'datasets', views.DatasetsViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^register/$', views.RegisterView.as_view(), name='user-register'),
    re_path(r'^login/$', views.LoginView.as_view(), name='user-login'),
    re_path(r'^logout/$', views.LogoutView.as_view(), name='user-logout'),
    re_path(r'^current/$', views.UserView.as_view(), name='user-current'),
    re_path(r'^change-password/$', views.ChangePasswordView.as_view(), name='change-password'),
    re_path(r'^change-password-2/$', views.ChangeUserPasswordView.as_view(), name='change-password-2'),
    re_path(r'^change-name-2/$', views.ChangeNameView.as_view(), name='change-name-2'),
    re_path(r'^delete-user-2/$', views.DeleteUserView.as_view(), name='delete-user'),
]
