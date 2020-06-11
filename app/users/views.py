from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from core.permissions import IsOwner
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     data = {
    #         "no content": "no content",
    #         "id": instance.id
    #     }
    #
    #     self.perform_destroy(instance)
    #     return Response(data, status=status.HTTP_204_NO_CONTENT)
    # #
    def destroy(self, request, *args, **kwargs):
        # print('delete to instance!')
        return super().destroy(request, *args, **kwargs)

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        elif self.action in ['update', 'destroy']:
            return [IsOwner()]
        return super().get_permissions()

    # @action(detail=False)
    # def fastcampus(self, request, *args, **kwargs):
    #     print('FC!!')
    #     return Response()
