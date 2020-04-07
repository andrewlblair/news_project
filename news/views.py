from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from news.models import Story


def index(request):
    story_list = Story.objects.order_by('-date')[:5]
    context_dict = {}
    context_dict['stories'] = story_list

    response = render(request, 'news/index.html', context=context_dict)
    return response

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('news:secret_news'))
            else:
                return HttpResponse("Your News account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'news/login.html')

@login_required()
def secret_news(request):
    story_list = Story.objects.order_by('-date')[:5]
    context_dict = {}
    context_dict['stories'] = story_list

    response = render(request, 'news/secret_news.html', context=context_dict)
    return response