from decimal import Decimal
from rest_framework import serializers
from store.models import Product, Collection


# using Serializer
# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    # define this field separately because this info is not available to serializer
    # marking as read_only because it is only going as response with data not allowed to write using POST
    products_count = serializers.IntegerField(read_only=True)


''' using Serializer
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all())

    # returns string representation of class
    # collection = serializers.StringRelatedField()

    # to include nested object
    # collection = CollectionSerializer()

    # to add a hyperlink for collection
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(), view_name='collection-detail')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
'''


# using ModelSerializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # by default PrimaryKeyRelatedField is used for Collection related model
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'price_with_tax', 'collection']

    #     fields = ['id', 'title', 'price', 'collection']
    # price = serializers.DecimalField(
    #     max_digits=6, decimal_places=2, source='unit_price')

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    # for HyperLinkRelatedField
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(), view_name='collection-detail')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # def validate
    # def create
    # def update
