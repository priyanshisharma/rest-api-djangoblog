from rest_framework.generics import ListAPIView
from reddjaapp.models import Post,Comment
from .serializers import PostSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer