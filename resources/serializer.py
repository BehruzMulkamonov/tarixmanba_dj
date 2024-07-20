from rest_framework import serializers

# from admin_panel.serializer.resources import Base64FileField, ResourceAdminSerializer
from resources.models import Category,  PeriodFilter, FilterCategories, Filters, Province, Resource,  \
    Attributes, Contents
import six
import base64
from django.core.files.base import ContentFile

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # If the base64 string is in the "data:" URL scheme, strip it off
            if data.startswith('data:image'):
                # Find the comma in the base64 string
                comma_index = data.find(',')
                if comma_index != -1:
                    data = data[comma_index+1:]

            # Decode the base64 string
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name
            file_name = self.get_file_name(decoded_file)
            data = ContentFile(decoded_file, name=file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_name(self, decoded_file):
        # Generate file name
        import uuid
        file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
        return '{}.png'.format(file_name)

# class PeriodFilterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PeriodFilter
#         fields = ['id', 'title', 'category',]


# class FilterCategoriesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FilterCategories
#         fields = ['id','title', 'category', ]


# class FiltersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Filters
#         fields = ['id','filter_category', 'title', ]


# class ProvinceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Province
#         fields = ['id','title', ]



# class AttributesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attributes
#         fields = ['id','resource_attribute', 'attributes_title', 'attributes_description', ]


# class ContentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contents
#         fields = ['id','resource_content', 'contents_title', 'contents_description']


# class FileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = File
#         fields = ['file']

# class ResourceSerializer(serializers.ModelSerializer):
#     category_name = serializers.SerializerMethodField()
#     filter_category_title = serializers.SerializerMethodField()
#     period_filter_title = serializers.SerializerMethodField()
#     image = Base64ImageField(required=False, allow_null=True)
#     files = FileSerializer(many=True, required=False, allow_null=True)
#     locations = serializers.StringRelatedField(many=True, required=False, allow_null=True)

#     class Meta:
#         model = Resource
#         fields = [
#             'category', 'filter_category', 'filters', 'period_filter', 'title',
#             'image', 'content', 'statehood', 'province', 'status', 'locations',
#             'files', 'link', 'video', 'category_name', 'filter_category_title',
#             'period_filter_title'
#         ]

#     def get_category_name(self, obj):
#         return obj.category.title if obj.category else None

#     def get_filter_category_title(self, obj):
#         return obj.filter_category.title if obj.filter_category else None

#     def get_period_filter_title(self, obj):
#         return obj.period_filter.title if obj.period_filter else None
        

   




# class CategorySerializer(serializers.ModelSerializer):
#     category = ResourceSerializer(many=True,read_only=True)
#     class Meta:
#         model = Category
#         fields = ['id','title', 'icon', 'order', 'category']
#     def get_category(self, obj):
#         return obj.category.all()


# class CategoryResourceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id','title', 'icon', 'order', ]



from rest_framework import serializers
from resources.models import Resource, Category, PeriodFilter, FilterCategories, Filters, Province
# from drf_extra_fields.fields import Base64ImageField

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PeriodFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodFilter
        fields = '__all__'

class FilterCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterCategories
        fields = '__all__'

class FiltersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filters
        fields = '__all__'

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    filter_category_title = serializers.SerializerMethodField()
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Resource
        fields = [
            'category', 'filter_category', 'filters', 'period_filter', 'title',
            'image', 'content', 'statehood', 'province', 'category_name',
            'filter_category_title'        ]

# , 'status', 'locations', 'files', 'link', 'video'

    def get_category_name(self, obj):
        return obj.category.title if obj.category else None

    def get_filter_category_title(self, obj):
        return obj.filter_category.title if obj.filter_category else None

class ResourceAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class CategoryResourceSerializer(serializers.ModelSerializer):
    category_resources = ResourceSerializer(many=True, source='category')

    class Meta:
        model = Category
        fields = ['id', 'title', 'icon', 'image', 'category_resources']









from rest_framework import serializers
from .models import Gallery, GalleryImages, File, FileFile, Audio, AudioFile, VirtualReality, VirtualRealityFile, Video, VideoFile, Location, AddLocation

class GalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImages
        fields = ('image',)

class GallerySerializer(serializers.ModelSerializer):
    gallery = GalleryImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ('id', 'title', 'image', 'gallery')

class FileFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileFile
        fields = ('file',)

class FileSerializer(serializers.ModelSerializer):
    file = FileFileSerializer(many=True, read_only=True)

    class Meta:
        model = File
        fields = ('id', 'title', 'file')

class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = ('file',)

class AudioSerializer(serializers.ModelSerializer):
    audio = AudioFileSerializer(many=True, read_only=True)

    class Meta:
        model = Audio
        fields = ('id', 'title', 'audio')

class VirtualRealityFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualRealityFile
        fields = ('file',)

class VirtualRealitySerializer(serializers.ModelSerializer):
    virtual_reality = VirtualRealityFileSerializer(many=True, read_only=True)

    class Meta:
        model = VirtualReality
        fields = ('id', 'title', 'audio', 'virtual_reality')

class VideoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoFile
        fields = ('file', 'link')

class VideoSerializer(serializers.ModelSerializer):
    video = VideoFileSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ('id', 'title', 'file', 'link', 'video')

class AddLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddLocation
        fields = ('latitude', 'longitude')

class LocationSerializer(serializers.ModelSerializer):
    location = AddLocationSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ('id', 'title', 'latitude', 'longitude', 'location')