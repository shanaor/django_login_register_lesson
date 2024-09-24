from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from base.models import Student
from base.serializers import StudentSerializer

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

# CRUD students
@api_view(['GET'])
def getStudents(request):
    all_students = StudentSerializer(Student.objects.all(), many=True).data
    return Response(all_students)


@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)