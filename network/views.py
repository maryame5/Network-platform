
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import *



def index(request):
    print("load ")
    user= request.user
    p=Post.objects.all()
    post = p.order_by("-timestamp").all()
    paginator = Paginator(post, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    return render(request, "network/index.html",{
        'user':user,
        'page_obj': page_obj,
        'page_number':page_number,
        "posts":post,})


@login_required
def following(request):
    user = request.user
    #get who this user is following
    foll= follow.objects.filter(follower=user)
    following_users = [f.following for f in foll] 
     #get the posts of the people they are following

    
    post=Post.objects.filter(user__in=following_users)
       
    
    
    post = post.order_by("-timestamp").all()

    paginator = Paginator(post, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "network/following.html",{
            "posts": post ,
             'page_obj': page_obj,
             'page_number':page_number,
             "following_users":following_users})

    



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
@csrf_exempt
@login_required
def create_post(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Load the JSON data
            userr = data.get("user")
            user= User.objects.get(username=userr) 
            content = data.get("content")
            if not content :
                return HttpResponse({"error":"content are required"} ,status=400)
            post = Post.objects.create(user=user, content=content)
            post.save()
        except json.JSONDecodeError:
            return  JsonResponse({"error": "Invalid JSON."}, status=400)
        except Exception as e:
            return JsonResponse({"error": "error"+str(e)}, status=500)
        
    return JsonResponse({"message": "post published successfully."}, status=201)

@csrf_exempt
@login_required
def edit(request,postId):
    posts=Post.objects.get(id=postId)
    if request.method == "PUT":
        try:
            data = json.loads(request.body)  # Load the JSON data
            contents = data.get("content")

            if not contents :
                return HttpResponse({"error":"content are required"} ,status=400)
            posts.content = contents
            posts.save()
            return JsonResponse({"message": "post edited successfully."}, status=201)
        except json.JSONDecodeError:
            return  JsonResponse({"error": "Invalid JSON."}, status=400)
        except Exception as e:
            return JsonResponse({"error": "error"+str(e)}, status=500)
        
    return JsonResponse({"message": "post edited successfully."}, status=201)


@csrf_exempt
def profil(request,name):  
     #normal user connect to network
     users= request.user
     user_name=User.objects.get(username=name)
     foll= follow.objects.filter(follower=user_name)
     following_users = [f.following for f in foll]
     following_nbr =len(following_users)
     follower_nbr=len(follow.objects.filter(following=user_name))
    
     #get the user who's creating this post
     userr = User.objects.get(username=name)
     #get tho posts of the one creating
     post = Post.objects.filter(user=userr)
     post = post.order_by("-timestamp").all()
     paginator = Paginator(post, 10)
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)
     
    
         
       
     return render(request, "network/profil.html",{
         "posts":post,
         "others":users,
         "userr":userr,
         "following_nbr":following_nbr,
         "follower_nbr":follower_nbr,
          'page_obj': page_obj,
         'page_number':page_number,

                  
                  })

@login_required
def follow_fun(request,following_name)   :
    if request.method == "POST":
            #user connected
            user=request.user
            following_user = User.objects.get(username=following_name)
            post_fo= Post.objects.filter(user=following_user).order_by('-id').first()
            #get the the creator of the post
                 #create relation between the user and the posts he wanna start following
            try :
                follow.objects.get(follower=user, following=following_user)
            
            except follow.DoesNotExist:

                 follow.objects.create(follower=user, following=following_user,post_fo=post_fo)
            return HttpResponseRedirect(reverse('profil', args=[following_name]))
    return JsonResponse({"error": "Invalid request method."}, status=405)
            


@login_required
def unfollow_fun(request,following_name)   :
    if request.method == "POST":
            #user connected
            user=request.user
            following_user = User.objects.get(username=following_name)
            post_fo= Post.objects.filter(user=following_user).order_by('-id').first()
            #get the the creator of the post
                 #create relation between the user and the posts he wanna start following
            try :
                follow.objects.get(follower=user, following=following_user).delete()
            
            except follow.DoesNotExist:

                message = "you should be following this user first "

                
            return HttpResponseRedirect(reverse('profil', args=[following_name]))
    return JsonResponse({"error": "Invalid request method."}, status=405)
            
def get_post(request,postId):
    try:
        post = Post.objects.get(id=postId)
        return JsonResponse({
            'id': post.id,
            'like':post.like,
            'content': post.content,
            'user': post.user.username,  # Assuming you want to send the username
            'timestamp': post.timestamp.isoformat()  # Format timestamp if needed
        })
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
@csrf_exempt
@login_required
def up_like(request,postId):
    if request.method == "POST":
        posts=Post.objects.get(id=postId)
        user = request.user
        like_list = posts.liked_by.all()
        if user in like_list:
            posts.liked_by.remove(user)
            posts.like = posts.liked_by.count()
            posts.save()
            return JsonResponse({"message": "unlike",
                                 "likes_count": posts.liked_by.count(),
                                 })
        else:
            posts.liked_by.add(user)
            posts.like =  posts.liked_by.count()
            posts.save()
           
            return JsonResponse({"message": "like",
                                 "likes_count": posts.liked_by.count(),
                                 })
        
