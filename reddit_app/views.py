from django.shortcuts import render, redirect
from reddit_app.forms import UserForm, UserProfileInfoForm, PostForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfileInfo, Post, Comment

# Create your views here.
@login_required
def special (request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return redirect('post_list')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'reddit_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('post_list')
            else: 
                return HttpResponse("Your account was inactive")
        else:
            print("Someone tried to login and failed")
            print(f'They used username: {username} and password: {password}')
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'reddit_app/login.html', {})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'reddit_app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'reddit_app/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            picture = form.cleaned_data.get('picture')
            content = form.cleaned_data.get('content')
            site_url = form.cleaned_data.get('site_url')
            post = Post(title=title, picture=picture, content=content, site_url=site_url, user=request.user)
            print(post)
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            print ('form is invalid')
    else:
        form = PostForm()
    return render(request, 'reddit_app/post_form.html', {'form': form})

@login_required
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            comment = Comment(content=content, user=request.user, post=request.post)
            print(comment)
            comment.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm()
    return render(request, 'reddit_app/comment_form.html', {'form': form})