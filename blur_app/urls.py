from .views.main_view import BlogView, BlogViewApp
from django.urls import path
from .views.auth_view import register_user, login_user
from .views.main_view import product_view, get_delete
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('blog/',BlogView.as_view()),
    path('blog/<int:id>', BlogViewApp.as_view()),
    path('register/',register_user),
    path('login/', login_user),
    path('token/refresh',TokenRefreshView.as_view()),
    path('view/', product_view),
    path('get_delete/<int:id>',get_delete)

]


