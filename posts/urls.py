from django.urls import path

from posts.views import posts_of_following_profiles

app_name='posts'

urlpatterns=[
    path('',posts_of_following_profiles,name='posts-follow-view'),
]