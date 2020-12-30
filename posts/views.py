from django.shortcuts import render
from profiles.models import Profile
from itertools import chain

# Create your views here.
def  posts_of_following_profiles(request):
    #get logged in user profile
    profile=Profile.objects.get(user=request.user)
    #check who we are following
    users=[user for user in profile.following.all()]
    posts=[]
    qs= None
    for u in users:
        p= Profile.objects.get(user=u)
        p_posts=p.post_set.all()
        posts.append(p_posts)
    my_posts = profile.profiles_posts()
    posts.append(my_posts)
    if len(posts)>0:
        qs=sorted(chain(*posts), reverse=True,key=lambda obj:obj.created)
    return render(request,'posts/main.html',{'profile':profile,'posts':qs})