from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandardUser

from .serializers import (ExperienceModelSerializer, ExperienceSerializer)
from .models import Experience

class ExperienceViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = ExperienceModelSerializer

    def get_queryset(self):
        """Restrict list to only user experience."""
        queryset = Experience.objects.filter(user=self.request.user)
        return queryset

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

        
    def create(self, request, *args, **kwargs):
        serializer = ExperienceSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = ExperienceModelSerializer(exp).data
        return Response(data, status=status.HTTP_201_CREATED)
        

    