from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import MedecineSerializers
from .serializers import PatientSerializers
from .serializers import RapportSerializers
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django.template import loader
from .models import Medecine
from .models import Infermier
from .models import Rapport
from .models import Patient




def login(request):
    return render(request,'./login.html')

def signUp(request):
    return render(request,'./signUp.html')


def signin(request):

    return render(request,'./singin.html')

def menu(request):
    return render(request,'./menu.html')

def absence(request):
    return render(request,'./absence.html')
def profile(request):
    return render(request,'./profile.html')
def planning(request):
    return render(request,'./planning.html')
def settings(request):
    return render(request,'./settings.html')



@api_view(['GET','DELET','ADD'])
def responce(request):
    x=[
        {
        'name':'rahma',
        'prenom':'alliouche',
        }
    ]


    return Response(x)
@api_view(['GET'])
def getrapp(request):
    rap= Rapport.objects.all()
    serializer= RapportSerializers(rap,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMeds(request):
    meds= Medecine.objects.all()
    serializer= MedecineSerializers(meds,many=True)
    return Response(serializer.data)


@api_view(['POST'])

def createRapp(request):
    data= request.data
    rap=Rapport.objects.create(
        text=data['text']
    )
    serializer = MedecineSerializers(rap,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    log=request.log
    med=Medecine.objects.create(
        email=log['email'],
        password=log['password'],
    )
    serializer =MedecineSerializers(med,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getPat(request):
    pat=Patient.objects.all()
    serializers=PatientSerializers(pat,many=True)
    return Response(serializers.data)

class UserListView(APIView):
    authentication_classes= [authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        username =[user.username for user in User.objects.all()]
        return Response(username)
    

class MedecineList(ListAPIView):
    queryset=Medecine.objects.all()
    serializer_class= MedecineSerializers


from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

