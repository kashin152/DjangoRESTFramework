from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from users.models import CustomsUser, Payments
from users.serializers import UserSerializer, PaymentsSerializer, CustomsUserDetailSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomsUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save()


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payment_method', 'paid_course', 'paid_lesson')
    ordering_fields = ('payment_date',)


class CustomsUserViewSet(viewsets.ModelViewSet):
    queryset = CustomsUser.objects.all()
    serializer_class = CustomsUserDetailSerializer
