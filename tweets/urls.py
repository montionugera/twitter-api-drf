from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tweets import views

urlpatterns = [
    path('tweets/', views.TweetList.as_view()),
    path('tweets/<int:pk>/', views.TweetDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

#http GET http://127.0.0.1:8000/tweets/
#http -a montionugera:1q2w3e4r --json POST http://127.0.0.1:8000/tweets/ body="I love cocoa"