from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogCustomSerializer(serializers.ModelSerializer):
    """ Custom Serializer """
    def create(self, validated_data):
        print('*** Custom Create method ***')
        return super(BlogCustomSerializer, self).create(validated_data)

    class Meta:
        model = Blog
        fields = '__all__'
