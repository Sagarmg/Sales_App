from rest_framework import serializers
from cart_app.models import Customer,CUSTOMER_STATUS, SKU,CartDetail


class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    code = serializers.CharField(max_length=10)
    address = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=50, allow_blank=True)
    zipcode  = serializers.CharField(max_length=10, required=False,allow_blank=True)
    status = serializers.IntegerField(default=0)

    def create(self, validated_data):
        """
        Create and return a new Customer instance, given the validated data.
        """
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Customer instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.status = validated_data.get('status', instance.status)
        instance.save()


class SKUSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ean_code = serializers.CharField(max_length=13)
    description = serializers.CharField(max_length=50, allow_blank=True)
    brand = serializers.CharField(max_length=100, allow_blank=True)
    category = serializers.CharField(max_length=100, allow_blank=True)
    colour = serializers.CharField(max_length=100, allow_blank=True)
    size = serializers.CharField(max_length=100, allow_blank=True)
    mrp = serializers.CharField(max_length=100,  default=0)
    length = serializers.FloatField(default=0)
    width = serializers.FloatField(default=0)
    weight = serializers.FloatField(default=0)

    def create(self, validated_data):
        """
        Create and return a new SKU instance, given the validated data.
        """
        return SKU.objects.create(**validated_data)


class CartSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    customer = CustomerSerializer(read_only=True)
    sku = SKUSerializer(many=True,read_only=True)
    customer_id = serializers.IntegerField(read_only=True)
    status = serializers.IntegerField(default=0)
    added_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()
    order_number = serializers.CharField(max_length=50)

    def create(self, validated_data):
        """
        Create and return a new SKU instance, given the validated data.
        """
        return CartDetail.objects.create(**validated_data)

