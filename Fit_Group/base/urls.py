from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('registration/',views.registrationPage,name='registration'),
    path('',views.home,name="home"),
    path('calendar/',views.calendar,name="calendar"),
    path("settings/",views.settings,name="settings"),
    path("groups/",views.groups,name="groups"),
    path("leaderboard/",views.leaderboard,name="leaderboard"),
    path('training_options/',views.training_options,name="training_options"),
    path("home/",views.home,name="home")
]