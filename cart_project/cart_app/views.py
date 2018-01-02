#+++++++++Django Package\Module +++++++++++++++++++++++
from django.shortcuts import render

#+++++++++DRF Package\Module +++++++++++++++++++++++
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

#+++++++++Project Package\Module +++++++++++++++++++++++
from .models import Customer, SKU, CartDetail
from serializers import CustomerSerializer,SKUSerializer,CartSerializer


class CustomerList(APIView):
    """
    List all Customer , or create a new Customer.
    """
    def get(self, request, format=None):
        customers = Customer.objects.all()
        resp = CustomerSerializer(customers, many=True)
        return Response(resp.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SKUList(APIView):
    """
    List all SKUs, or create a new SKU.
    """
    def get(self, request, format=None):
        skus = SKU.objects.all()
        serializer = SKUSerializer(skus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SKUSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    """
    Retrieve or delete a Customer instance.
    """
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SKUDetail(APIView):
    """
    Retrieve or delete a SKU instance.
    """
    def get_object(self, pk):
        try:
            return SKU.objects.get(pk=pk)
        except SKU.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sku = self.get_object(pk)
        serializer = SKUSerializer(sku)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        sku = self.get_object(pk)
        sku.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartList(APIView):
    """
    List all CustomerCart , or create a new CustomerCart.
    """
    def get(self, request, format=None):
        carts = CartDetail.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        customer_id = request.data['customer_id']
        skus_list = request.data['sku']
        try:
            customer = Customer.objects.get(id=int(customer_id))
            skus = SKU.objects.filter(ean_code__in=skus_list)
            cart = CartDetail.objects.create(customer=customer)
            cart.sku.add(*skus)
            cartdetail = CartDetail.objects.filter(id=cart.id)
            serializer = CartSerializer(cartdetail, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CARTDetail(APIView):
    """
    Retrieve or delete a Customer instance.
    """
    def get_object(self, pk):
        try:
            return CartDetail.objects.get(pk=pk)
        except CartDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cart = self.get_object(pk)
        if request.data.get('add_sku'):
            skus_list = request.data.get('add_sku')
            skus = SKU.objects.filter(ean_code__in=skus_list)
            cart.sku.add(*skus)
            cartdetail = CartDetail.objects.filter(id=cart.id)
            serializer = CartSerializer(cartdetail, many=True)
            return Response(serializer.data)
        elif request.data.get('remove_sku'):
            skus_list = request.data.get('remove_sku')
            skus = SKU.objects.filter(ean_code__in=skus_list)
            cart.sku.remove(*skus)
            cartdetail = CartDetail.objects.filter(id=cart.id)
            serializer = CartSerializer(cartdetail, many=True)
            return Response(serializer.data)

