
from rest_framework import serializers
from .models import GeeksModel
from django.db import models


class GeersListSerializer( serializers.Serializer ) :
    title = serializers.CharField(max_length = 50)
    image = serializers.ImageField()

    def create(self, validated_data):
        
        title = validated_data.pop('title')
        image = validated_data.pop('image')
        user = User.objects.latest('created_at')
        for titl, img in zip(title, image):
            geeks = GeeksModel.objects.create(title=titl, image=img, **validated_data)
    
        return geeks

class GeeksSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeeksModel
        fields = ('title', 'image', 'user')
















"""class GeeksSerializer(ModelSerializer): 
    
    class Meta: 
        model = GeeksModel
        fields = ['title', 'image']"""






"""class GeeksSerializer(ModelSerializer): 
    class Meta: 
        model = GeeksModel
        fields = ('title', 'image')"""

    



