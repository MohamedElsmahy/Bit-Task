from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

''' Funcation Viwes '''


# @api_view(['GET'])
# def product_list_api(request):
#     all_products = Product.objects.all()
#     data = ProductSerializer(all_products, many=True).data
#     return Response({'products': data})

''' Generics Viwes '''


class ProductsApi(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


''' Class Based Viwes '''


class GetProducts(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        try:
            products = Product.objects.all()
            products = ProductSerializer(products, many=True)
            return Response({"products": products.data})
        except Exception:
            return Response({'error': "error while get products"})


# class AddProduct(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         user = self.request.user
#         data = self.request.data
#         try:
#             Product.objects.create(
#                 name=data["name"],
#                 price=data["price"],
#                 seller=user,
#             )
#             return Response({'success': "Product added successfully"})
#         except Exception as e:
#             return Response({'error': e.args})
