from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView

app_name = 'accounts'
urlpatterns = [
    path('api/register/', RegisterView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/user/', UserView.as_view()),
    path('api/logout/', LogoutView.as_view()),
]
