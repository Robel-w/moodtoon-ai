from django.urls import path
from .views import Login, RegisterUser, Logout, profile

urlpatterns = [
    path("login/", Login.as_view(), name="login"),# as_view changes cas based views to callable views
    path("register/", RegisterUser.as_view(), name="register"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
]