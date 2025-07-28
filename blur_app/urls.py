from .views.main_view import BlogView, BlogViewApp
from django.urls import path
from .views.auth_view import register_user, login_user
from .views.main_view import product_view, get_delete, category_view, update_del_product
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('blog/',BlogView.as_view()),
    path('blog/<int:id>', BlogViewApp.as_view()),
    path('register/',register_user),
    path('login/', login_user),
    path('token/refresh',TokenRefreshView.as_view()),
    path('category/', category_view),
    path('update_category/<int:id>',get_delete),
    path('product/', product_view),
    path('update_product/<int:id>', update_del_product)

]


