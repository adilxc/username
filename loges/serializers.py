from rest_framework import serializers

from loges.models import Registration


class LogSerializers(serializers.ModelSerializer):
    class Meta:
       model = Registration
       fields ='__all__'