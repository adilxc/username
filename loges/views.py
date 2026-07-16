from rest_framework import viewsets


from loges.models import Registration
from loges.serializers import LogSerializers


class nameview(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = LogSerializers