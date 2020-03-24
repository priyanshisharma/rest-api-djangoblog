from . models import Post
from django.utils.deprecation import MiddlewareMixin

class GetAuthor(MiddlewareMixin):

    def process_request(self,request):
        print("These are the creators!")
        