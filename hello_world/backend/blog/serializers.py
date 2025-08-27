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
    """Exploring SerializerMethodField"""
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
    """Customizing field-level validation"""
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
    """Defining a custom field-level validator"""
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

#######################

class BlogCustom9Serializer(serializers.ModelSerializer):
    """Performing object-level validation"""
    def validate(self, attrs):
        if attrs["title"] == attrs["content"]:
            raise serializers.ValidationError("Title and content cannot have value")
        return attrs

    class Meta:
        model = Blog
        fields = "__all__"


#######################
def custom_obj_validator(attrs):
    """Defining custom object-level validators"""
    print("custom object validator")
    if attrs["title"] == attrs["content"]:
        raise serializers.ValidationError("Title and content cannot have the same")
    return attrs


class BlogCustom10Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        validators = [custom_obj_validator]

#######################

def func_validator(attr):  # 1- Evaluates first
    """ The order of the evaluation of validators """
    print("func val")
    if "*" in attr:
        raise serializers.ValidationError("Illegal char")
    return attr


class BlogCustom11Serializer(serializers.ModelSerializer):
    def validate_title(self, value):  # 2-If func_validator succeeds
        print("validate_title method")
        if "_" in value:
            raise serializers.ValidationError("Illegal char")
        return value

    def validate(self, attrs):  # 3- If all field validator succeeds
        print("main validate method")
        return attrs

    class Meta:
        model = Blog
        fields = "__all__"
        extra_kwargs = {"title": {"validators": [func_validator]}}


#######################
class BlogCustom12Serializer(serializers.ModelSerializer):
    """Remove default validators from the DRF Serializer class"""
    class Meta:
        model = Blog
        fields = "__all__"
        validators = []


#######################
class BlogCustom13Serializer(serializers.ModelSerializer):
    """Using to_internal_value"""
    def to_internal_value(self, data):
        print("before validation", data)
        return super().to_internal_value(data)

    class Meta:
        model = Blog
        fields = "__all__"

#######################

class BlogCustom14Serializer(serializers.ModelSerializer):
    """Using to_representation"""
    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp["title"] = resp["title"].upper()
        return resp

    class Meta:
        model = Blog
        fields = "__all__"

#######################

class BlogCustom15Serializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        print('Printing context –', self.context)
        return super().to_internal_value(data)

    class Meta:
        model = Blog
        fields = '__all__'

#######################

class CustomPKRelatedField(serializers.PrimaryKeyRelatedField):
    """Passing a custom QuerySet to PrimaryKeyField"""
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
