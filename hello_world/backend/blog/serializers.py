from rest_framework import serializers
from rest_framework import validators
from blog.models import Blog, CoverImage, Tags
from author.models import Author


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

#######################

class BlogCustom2Serializer(serializers.ModelSerializer):
    """ Custom update method """
    def update(self, instance, validated_data):
        print('*** Custom Update method')
        return super(BlogCustom2Serializer, self).update(instance, validated_data)

#######################

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

#######################

class BlogCustom5Serializer(serializers.ModelSerializer):
    word_count = serializers.SerializerMethodField()

    def get_word_count(self, obj):
        return len(obj.content.split())

    class Meta:
        model = Blog
        fields = '__all__'

#######################

class BlogCustom6CustomSerializer(serializers.ModelSerializer):
    word_count = serializers.SerializerMethodField(method_name="use_custom_word_count")

    def use_custom_word_count(self, obj):
        return len(obj.content.split())

    class Meta:
        model = Blog
        fields = "__all__"

#######################

class BlogCustom7Serializer(serializers.ModelSerializer):
    def validate_title(self, value):
        print("validate_title method")
        if "_" in value:
            raise serializers.ValidationError("illegal char")
        return value

    class Meta:
        model = Blog
        fields = "__all__"

#######################

def demo_func_validator(attr):
    print('func val')
    if '_' in attr:
        raise serializers.ValidationError('invalid char')
    return attr


class BlogCustom8Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        extra_kwargs = {
            "title": {"validators": [demo_func_validator]},
            "content": {"validators": [demo_func_validator]},
        }


class BlogCustom15Serializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        print('Printing context –', self.context)
        return super().to_internal_value(data)

    class Meta:
        model = Blog
        fields = '__all__'

class CustomPKRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        req = self.context.get('request', None) # context value
        queryset = super().get_queryset() # retrieve default filter
        if not req:
            return None
        return queryset.filter(user=req.user) # additional filter


class BlogCustom16Serializer(serializers.ModelSerializer):
    tags = CustomPKRelatedField(queryset=Tags.objects.all())

    class Meta:
        model = Blog
        fields = '__all__'
