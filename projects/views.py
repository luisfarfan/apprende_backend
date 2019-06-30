from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from projects.models import Projects
from projects.serializer import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()
