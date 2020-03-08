from rest_framework.generics import ListAPIView , RetrieveAPIView
from reddjaapp.models import Post,Comment
from .serializers import PostSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer