from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.models import Student

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


@api_view(['GET'])
def getStudents(request):
    res=[] #create an empty list
    for img in Student.objects.all(): #run on every row in the table...
        res.append({
                "sName":img.sName,
               "image":str( img.image)
                }) #append row by to row to res list
    return Response(res) #return array as json response

#   image = models.ImageField(null=True,blank=True,default='/placeholder.png')
#     id = models.BigAutoField(primary_key=True)
#     sName = models.CharField(max_length=20)
#     age = models.FloatField()