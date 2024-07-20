from django.contrib import admin
from django import forms
from .models import Category, FilterCategories, PeriodFilter, Filters, Resource, Province, \
    Gallery, GalleryImages, File, FileFile, Audio, AudioFile, VirtualReality, VirtualRealityFile, Video, \
    VideoFile, Location, AddLocation, Contents, Attributes


admin.site.register(Category)
admin.site.register(FilterCategories)
admin.site.register(PeriodFilter)
admin.site.register(Filters)
admin.site.register(Province)


class ResourceAdminForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance


class AttributesInline(admin.TabularInline):
    model = Attributes
    extra = 1


class ContentsInline(admin.TabularInline):
    model = Contents
    extra = 1


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1


class GalleryImagesInline(admin.TabularInline):
    model = GalleryImages
    extra = 1


class FileInline(admin.TabularInline):
    model = File
    extra = 1


class FileFileInline(admin.TabularInline):
    model = FileFile
    extra = 1


class AudioInline(admin.TabularInline):
    model = Audio
    extra = 1


class AudioFileInline(admin.TabularInline):
    model = AudioFile
    extra = 1


class VirtualRealityInline(admin.TabularInline):
    model = VirtualReality
    extra = 1


class VirtualRealityFileInline(admin.TabularInline):
    model = VirtualRealityFile
    extra = 1


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1


class VideoFileInline(admin.TabularInline):
    model = VideoFile
    extra = 1


class LocationInline(admin.TabularInline):
    model = Location
    extra = 1


class AddLocationInline(admin.TabularInline):
    model = AddLocation
    extra = 1

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.resource = form.instance
                instance.save()
            formset.save_m2m()

    class Media:
        js = (
            "dropdown.js",
            "https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js",
        )


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'statehood',)
    search_fields = ('title',)
    inlines = [
        AttributesInline, ContentsInline, GalleryInline, FileInline, AudioInline, VirtualRealityInline, VideoInline, LocationInline, AddLocationInline
    ]
