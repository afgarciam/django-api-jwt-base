from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import PersonSerializer
from .models import Person

# Create your views here.

# class PersonView(APIView):
#     permission_classes = (IsAuthenticated,)

@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def get_persons(request, format=None):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)

