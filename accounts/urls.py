from django.urls import path
from .views import RegisterView, UserView  # , LogoutView, login_view#user,
from rest_framework_simplejwt import views as jwt_viwes

app_name = 'accounts'

urlpatterns = [
    # with simple jwt auth
    path('api/login/', jwt_viwes.TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', jwt_viwes.TokenRefreshView.as_view()),

    # path('api/v2/user/', user, name='user'),
    path('api/register/', RegisterView.as_view()),
    # path('api/login/', LoginView.as_view()),
    path('api/user/', UserView.as_view(), name='user'),
    # path('api/logout/', LogoutView.as_view()),
    # path('api/v2/login/', login_view, name='login'),
]
