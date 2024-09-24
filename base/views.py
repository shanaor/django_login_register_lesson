from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

@api_view(['GET'])
def index(req):
    return Response('hello')

@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = False
    user.is_superuser=True
    user.save()
    return Response("new user born")


# login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom columns
        token['bbbb'] ="blabla"
        token['username'] = user.username
        token['emaillll'] = user.email
        # ...
        return token




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# public
@api_view(['GET'])
def test_pub(req):
    return Response('test public zone')

# private
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_pri(req):
    print(req.user)
    return Response('test private zone')