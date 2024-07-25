from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Medium, Collection, IACollection

class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ["id", "username", "password"]
      extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validated_data):
      print(validated_data)
      user = User.objects.create_user(**validated_data)
      return user


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
      model = Collection
      fields = ['name']


class IACollectionSerializer(serializers.ModelSerializer):
    class Meta:
      model = IACollection
      fields = ['name']


class MediaSerializer(serializers.ModelSerializer):
    collections = CollectionSerializer(many=True)
    ia_collections = IACollectionSerializer(many=True)
    
    class Meta:
      model = Medium
      fields = ["user", "identifier",  "mediatype", "date", "description", "language", "title",  "url", "collections", "ia_collections"]
      extra_kwargs = {"user": {"read_only": True}}
    
    def create(self, validated_data):
      collections_data = validated_data.pop("collections")
      ia_collections_data = validated_data.pop("ia_collections")
      media = Medium.objects.create(**validated_data)
      for collection_data in collections_data:
        Collection.objects.create(medium=media, **collection_data)
      for ia_collection_data in ia_collections_data:
        IACollection.objects.create(medium=media, **ia_collection_data)
      return media