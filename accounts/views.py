from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.exceptions import AuthenticationFailed
# import jwt
# import datetime
# from .models import MyUser
from .serializers import UserSerializer
from rest_framework.response import Response
# from rest_framework import exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.decorators import api_view
# from django.views.decorators.csrf import ensure_csrf_cookie
# from .auth import generate_access_token, generate_refresh_token
# from django.views.decorators.csrf import csrf_protect


# Create your views here.


# @api_view(['GET'])
# def user(request):
#     user = request.user
#     serialized_user = UserSerializer(user).data
#     return Response({'user': serialized_user})


''' Registeration '''


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# class LoginView(APIView):
#     permission_classes = (AllowAny,)
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']

#         user = MyUser.objects.filter(email=email).first()

#         if user is None:
#             raise AuthenticationFailed('User not found')

#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password')

#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload, 'secret',
#                            algorithm='HS256')

#         response = Response()

#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token
#         }
#         return response


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
            'id': request.user.id,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
            'email': request.user.email,
            'password': request.user.password,
        }
        return Response(content)


''' Login API '''

# @api_view(['POST'])
# @permission_classes([AllowAny])
# @ensure_csrf_cookie
# def login_view(request):
#     email = request.data.get('email')
#     password = request.data.get('password')
#     response = Response()
#     if (email is None) or (password is None):
#         raise exceptions.AuthenticationFailed(
#             'username and password required')

#     user = MyUser.objects.filter(email=email).first()
#     if(user is None):
#         raise exceptions.AuthenticationFailed('user not found')
#     if (not user.check_password(password)):
#         raise exceptions.AuthenticationFailed('wrong password')

#     serialized_user = UserSerializer(user).data

#     access_token = generate_access_token(user)
#     refresh_token = generate_refresh_token(user)

#     response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
#     response.data = {
#         'access_token': access_token,
#         'user': serialized_user,
#     }

#     return response


''' Logout API '''

# class LogoutView(APIView):
#     def post(self, request):
#         response = Response()
#         response.delete_cookie('access_token')
#         response.data = {
#             'message': 'logout successfully'
#         }
#         return response
