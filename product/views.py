from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer





@api_view(['GET'])
def get_products(request):

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response({'products': serializer.data})

@api_view(['POST'])
def create_product(request):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_one_product(request, pk):

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product)
    return Response({'product': serializer.data})

@api_view(['PATCH', 'PUT'])
def update_product(request, pk):

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product, data = request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response({'product': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product(request, pk):

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
