from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register(r'userrole', views.UserRoleViewSet, basename='userrole')
router.register(r'usertheme', views.UserThemeViewSet, basename='usertheme')


urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('signup/', views.register_view, name='register_view'),
    path('profil/<id>/', views.profile_page, name='profile_page'),
    path('', views.home_page, name='home_page'),
    path('/home', views.home_page, name='home_page'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(router.urls)),
]

