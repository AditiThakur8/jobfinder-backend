from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Job Finder API</h1>")

class JobsViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-date_posted')
    serializer_class = JobSerializer

