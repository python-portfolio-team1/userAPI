from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('login/',views.login, name = 'login'),
    path('profile/',views.profile, name = 'profile'),
    path('users/', views.users_list),
    path('users/<int:id>', views.users_detail)
    ]