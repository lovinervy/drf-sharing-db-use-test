import os
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from .models import Product

class CustomModelViewSet(ModelViewSet):
    using: str | None = None

    def remote_create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.using is None:
            return
        Model = self.get_queryset().model
        instance = Model.objects.using(self.using).create(**serializer.data)
        return instance

    def perform_create(self, serializer, share_id):
        Model = self.get_queryset().model
        instance = Model.objects.create(**serializer.data)
        instance.share_id = share_id
        instance.save()
        return self.get_serializer(instance)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        remote_instance = self.remote_create(request)
        data = request.data.copy()
        share_id = None
        if remote_instance is not None:
            share_id = remote_instance.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer = self.perform_create(serializer, share_id)
        headers = self.get_success_headers(serializer.data)
        remote_instance.local_id = serializer.data['id']
        remote_instance.project_from = os.environ.get('PROJECT_NAME', '')
        remote_instance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('local_id', 'share_id', 'project_from')


class ProductViewSet(CustomModelViewSet):
    using = 'share'
    permission_classes = [AllowAny]
    pagination_class = None
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
