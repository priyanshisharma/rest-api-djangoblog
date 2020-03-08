from rest_framework import serializers
from reddjaapp.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author','title','text','create_date','published_date']
