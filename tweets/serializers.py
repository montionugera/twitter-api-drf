from django.contrib.auth.models import User
from rest_framework import serializers
from tweets.models import Tweet



class TweetSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_retweet = serializers.ReadOnlyField(source='is_retweet')
    class Meta:
        model = Tweet
        fields = ['id', 'body','author','is_retweet']


class UserSerializer(serializers.ModelSerializer):
    tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=Tweet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']