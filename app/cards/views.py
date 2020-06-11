from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cards.models import Card
from cards.permissions import CardPermission
from cards.serializers import CardSerializer


class CardModelViewSetAPI(viewsets.ModelViewSet):
    permission_classes = [
        CardPermission,
    ]
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )

