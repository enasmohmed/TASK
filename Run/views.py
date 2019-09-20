from django.shortcuts import render, render_to_response

# Create your views here.
from rest_framework import status, permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Run.models import Person
from Run.serializers import PersonSerializer


def home(request):
    return render_to_response('index.html')





class PersonViewSet(ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset  = Person.objects.all()
    serializer_class = PersonSerializer



