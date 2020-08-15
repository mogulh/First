from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="feed_home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name="profile"),
    path('settings/', views.settings, name="settings"),


]
