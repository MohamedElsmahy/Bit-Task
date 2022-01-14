from django.urls import path
from .views import GetProducts, ProductsApi, AddProduct

app_name = 'products'

urlpatterns = [
    path('api/userproducts/', GetProducts.as_view()),
    path('api/addproduct/', AddProduct.as_view()),
    path('api/allproducts/', ProductsApi.as_view()),
    # path('api/v2/addproducts/', AddProductsApi.as_view()),
]
