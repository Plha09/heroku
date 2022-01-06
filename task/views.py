from django.shortcuts import render
from rest_framework import generics
from task.models import Students
from task.serializers import StudentSerializer
# Create your views here.

class StudentList(generics.ListCreateAPIView):
	queryset = Students.objects.all()
	serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Students
	serializer_class = StudentSerializer
