from rest_framework import serializers
from rest_framework import validators
from blog.models import Blog, CoverImage, Tags
from author.models import Author
from 

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogCustomSerializer(serializers.ModelSerializer):
    """ Custom Create method """
    def create(self, validated_data):
        print('*** Custom Create method ***')
        return super(BlogCustomSerializer, self).create(validated_data)

    class Meta:
        model = Blog
        fields = '__all__'

class BlogCustom2Serializer(serializers.ModelSerializer):
    """ Custom update method """
    def update(self, instance, validated_data):
        print('*** Custom Update method')
        return super(BlogCustom2Serializer, self).update(instance, validated_data)

class BlogCustom3Serializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tags.objects.all(), many=True, allow_empty=True
    )
    cover_image = serializers.PrimaryKeyRelatedField(
        queryset=CoverImage.objects.all(), validators=[validators.UniqueValidator(CoverImage.objects.all())]
    )
    class Meta:
        model = Blog
        fields = '__all__'

class BASerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'bio']

class BlogCustom4Serializer(serializers.ModelSerializer):
    author_details = BASerializer(source='author')
    
    class Meta:
        model = Blog
        fields = '__all__'
