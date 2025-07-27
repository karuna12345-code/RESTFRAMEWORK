from .views.main_view import BlogView, BlogViewApp
from django.urls import path
from .views.auth_view import register_user, login_user
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('blog/',BlogView.as_view()),
    path('blog/<int:id>', BlogViewApp.as_view()),
    path('register/',register_user),
    path('login/', login_user),
    path('token/refresh',TokenRefreshView.as_view())

]


