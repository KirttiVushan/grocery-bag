from bag.models import Groceries
from bag.api.serializers import Groceries_serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class Groceries_view(viewsets.ModelViewSet):
    queryset = Groceries.objects.all()
    serializer_class = Groceries_serializers
  
