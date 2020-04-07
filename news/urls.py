from django.urls import path
from news import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name="login"),
    path('secret_news/', views.secret_news, name="secret_news"),
]