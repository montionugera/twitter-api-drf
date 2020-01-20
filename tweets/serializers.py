from django.contrib.auth.models import User
from rest_framework import serializers
from tweets.models import Tweet



class TweetSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Tweet
        fields = ['id', 'body','author']


class UserSerializer(serializers.ModelSerializer):
    tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=Tweet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']