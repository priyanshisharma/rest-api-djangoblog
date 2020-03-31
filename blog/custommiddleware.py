from . models import Post
from django.utils.deprecation import MiddlewareMixin

class GetAuthor(MiddlewareMixin):

    def process_request(self,request):
        print(request.headers)
        