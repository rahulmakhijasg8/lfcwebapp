from django.core.exceptions import ValidationError
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Order, OrderItem, Product, Customer, Reviews

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price','tax_price']

    tax_price = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.price*1.1

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['User','name','email']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id','product','name','description','date']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only = True)
    total_price = serializers.SerializerMethodField()
    
    def get_total_price(self, cart_item:OrderItem):
        return cart_item.quantity*cart_item.product.price
    
    class Meta:

        model = OrderItem
        fields = ['id','product','quantity','total_price']

class AddCartItemSerializer(serializers.ModelSerializer):
    
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise ValidationError('No Product with the given ID was found.')
        return value



    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            #cart_item = OrderItem.objects.get(cart_id = cart_id,product_id=product_id)
            cart_item = OrderItem.objects.get(product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item

        except OrderItem.DoesNotExist:
            self.instance = OrderItem.objects.create(cart_id = cart_id, **self.validated_data)
        
        return self.instance

    class Meta:
        model = OrderItem
        fields = ['id','product_id','quantity']

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    items = CartItemSerializer(many = True, read_only = True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart):
        return sum([item.quantity * item.product.price for item in cart.items.all()])

    class Meta:
        model = Order
        fields = ['id', 'items','total_price']


