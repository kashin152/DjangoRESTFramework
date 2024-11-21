from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserProfileViewSet, PaymentsViewSet, CustomsUserViewSet


app_name = UsersConfig.name


router = DefaultRouter()
router.register(r'profile', UserProfileViewSet, basename='user-profile')
router.register(r'payments', PaymentsViewSet, basename='payments')
router.register(r'users', CustomsUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]