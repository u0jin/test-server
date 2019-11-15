from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User , Group 
from .models import Board
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer , BoardSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer    

