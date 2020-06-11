from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

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
