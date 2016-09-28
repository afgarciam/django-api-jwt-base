from rest_framework import routers, serializers, viewsets
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name','last_name')