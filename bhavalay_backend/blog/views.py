# views.py
from rest_framework import generics, permissions
from .models import Blog
from .serializers import BlogSerializer
from django.http import HttpResponse
def hm(request):
    return HttpResponse("<h1>deployed project</h1>")
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer