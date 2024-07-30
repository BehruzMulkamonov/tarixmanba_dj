from django.contrib import admin
from django import forms
from .models import Category, FilterCategories, PeriodFilter, Filters, Resource, Province, \
    Gallery, File, Audio, VirtualReality, Video, \
    Location, Contents, Attributes


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


class FileInline(admin.TabularInline):
    model = File
    extra = 1


class AudioInline(admin.TabularInline):
    model = Audio
    extra = 1


class VirtualRealityInline(admin.TabularInline):
    model = VirtualReality
    extra = 1


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1


class LocationInline(admin.TabularInline):
    model = Location
    extra = 1


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'statehood',)
    search_fields = ('title',)
    inlines = [
        AttributesInline, ContentsInline, GalleryInline, FileInline,\
        AudioInline, VirtualRealityInline, VideoInline, LocationInline,]
