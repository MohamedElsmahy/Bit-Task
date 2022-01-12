from django.urls import path
from .views import GetProducts, ProductsApi

app_name = 'products'

urlpatterns = [
    path('api/products/', GetProducts.as_view()),
    # path('api/addproduct/', AddProduct.as_view()),
    path('api/v2/products/', ProductsApi.as_view()),
]
