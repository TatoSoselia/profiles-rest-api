from rest_framework import (
    viewsets,
    filters
)
from rest_framework.authentication import TokenAuthentication

from profiles import (
    serializers,
    models,
    permission
)


class UserView(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permission.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
