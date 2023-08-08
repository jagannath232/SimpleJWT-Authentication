from django.shortcuts import render
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import BasicAuthentication,SessionAuthentication

# create view here
class StudentModelViewset(viewsets.ModelViewSet):
      queryset = Student.objects.all()
      serializer_class = StudentSerializer
      permission_classes = [IsAuthenticated]
      authentication_classes = [JWTAuthentication]
