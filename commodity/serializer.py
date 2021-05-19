from rest_framework import serializers

from .models import Category, Factory, Car, CustomerTrade, FactoryTrade


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'cat_id',
            'cat_name',
            'cat_pid',
            'cat_level',
            'children'
        )


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = (
            'fid',
            'fname',
            'faddress'
        )


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'cid',
            'cname',
            'cbrand',
            'introduce',
            'pics',
            'cprice',
            'fid'
        )


class CustomerTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerTrade
        fields = (
            'ctid',
            'ctprice',
            'cprofit',
            'cid'
        )


class FactoryTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryTrade
        fields = (
            'ftid',
            'ftprice',
            'fid'
        )
