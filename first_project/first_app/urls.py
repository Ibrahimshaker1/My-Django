from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.register, name='index'),
    path('other', views.other, name='other'),
    path("relative", views.relative, name="relative"),
    path("logout/", views.user_logout, name="logout"),
    path("special/", views.special, name="special"),
    path("user_login/", views.user_login, name="user_login")
]
