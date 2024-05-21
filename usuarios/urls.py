from usuarios.views.login import Login
from usuarios.views.register import Register
from usuarios.views.user import User

from django.urls import path

urlpatterns = [
    path('login', Login.as_view()),
    path('register', Register.as_view()),
    path('user', User.as_view()),
    path('user/<int:id>', User.as_view())
]
