from django.contrib import admin
# from unfold.admin import ModelAdmin
from .models import Category, FilterCategories, PeriodFilter, Filters,  Resource, Province, \
        Gallery, GalleryImages, File, FileFile, Audio, AudioFile, VirtualReality, VirtualRealityFile, Video, \
        VideoFile, Location, AddLocation
from django import forms


admin.site.register(Category)
admin.site.register(FilterCategories)
admin.site.register(PeriodFilter)
admin.site.register(Filters)
# admin.site.register(File)
# admin.site.register(Location)
admin.site.register(Province)



# @admin.register(Resource)
# class ResourseModelAdmin(admin.ModelAdmin):
#     list_display = ["title", "category"]

#     class Media:
#         js = (
#             "dropdown.js",
#             "https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js",
#         )



# class GalleryImagesInline(admin.TabularInline):
#     model = GalleryImages

# @admin.register(Gallery)
# class GalleryAdmin(admin.ModelAdmin):
#     inlines = [GalleryImagesInline]


# class FileFileInline(admin.TabularInline):
#     model = FileFile

# @admin.register(File)
# class FileAdmin(admin.ModelAdmin):
#     inlines = [FileFileInline]


# class AudioFileInline(admin.TabularInline):
#     model = AudioFile

# @admin.register(Audio)
# class AudioAdmin(admin.ModelAdmin):
#     inlines = [AudioFileInline]


# class VirtualRealityFileInline(admin.TabularInline):
#     model = VirtualRealityFile

# @admin.register(VirtualReality)
# class VirtualRealityAdmin(admin.ModelAdmin):
#     inlines = [VirtualRealityFileInline]


# class VideoFileInline(admin.TabularInline):
#     model = VideoFile

# @admin.register(Video)
# class VideoAdmin(admin.ModelAdmin):
#     inlines = [VideoFileInline]


# class AddLocationInline(admin.TabularInline):
#     model = AddLocation

# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     inlines = [AddLocationInline]

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


class GalleryImagesInline(admin.TabularInline):
    model = GalleryImages



class FileFileInline(admin.TabularInline):
    model = FileFile

    
class AudioFileInline(admin.TabularInline):
    model = AudioFile


class VirtualRealityFileInline(admin.TabularInline):
    model = VirtualRealityFile

    
class VideoFileInline(admin.TabularInline):
    model = VideoFile


class AddLocationInline(admin.TabularInline):
    model = AddLocation

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    form = ResourceAdminForm
    list_display = ["title", "category"]
    inlines = [
        GalleryImagesInline,
        FileFileInline,
        AudioFileInline,
        VirtualRealityFileInline,
        VideoFileInline,
        AddLocationInline,
    ]

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


# admin.site.register(GalleryImages)
# admin.site.register(FileFile)
# admin.site.register(AudioFile)
# admin.site.register(VirtualRealityFile)
# admin.site.register(VideoFile)
# admin.site.register(AddLocation)