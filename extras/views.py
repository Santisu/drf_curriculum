from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandardUser

from .serializers import ExtraModelSerializer, ExtraSerializer
from .models import Extra


class ExtraViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = ExtraModelSerializer

    def get_queryset(self):
        """Restrict list to only user extras."""
        queryset = Extra.objects.filter(user=self.request.user)
        return queryset

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

        
    def create(self, request, *args, **kwargs):
        serializer = ExtraSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        extra = serializer.save()
        data = ExtraModelSerializer(extra).data
        return Response(data, status=status.HTTP_201_CREATED)
        

    