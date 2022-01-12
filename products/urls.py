from django.urls import path
from . import api

app_name = 'products'

urlpatterns = [
    # path('signup/', views.get_user_type , name = 'signup'),
    #APIS
    path('signup/',api.UserSignupView.as_view(),name="signup"),
    path('authenticated/',api.CkeckAuthenticatedView.as_view(),name="authenticated"),
    path('login/',api.LoginView.as_view(),name="login"),
  
]