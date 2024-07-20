from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=255)
    icon = models.FileField(blank=True, null=True, upload_to="icons/")  # shunga iconca kodi yozilidi
    image = models.FileField(blank=True, null=True, upload_to="icons/")  # shunga iconca kodi yozilidi
    order = models.IntegerField()
    interactive = models.BooleanField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class PeriodFilter(BaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 related_name='category_filter')

    class Meta:
        verbose_name = 'Period Filter'
        verbose_name_plural = 'Period Filters'

    def __str__(self):
        return self.title


class FilterCategories(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 related_name='categories')
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Filter Category'
        verbose_name_plural = 'Filter Categories'

    def __str__(self):
        return self.title


class Filters(BaseModel):
    filter_category = models.ForeignKey(FilterCategories, on_delete=models.SET_NULL, null=True,
                                        related_name='filters_category')
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Filter'
        verbose_name_plural = 'Filters'

    def __str__(self):
        return self.title


class Province(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'


# class Interive(BaseModel):
#     class Status(models.TextChoices):
#         GALLERY = 'Gl', 'Gallery'
#         AUDIO = 'AU', 'Audio'
#         FILE = 'Fl', 'File'
#         VIRTUAL_REALITY = 'VR', 'Virtual_reality'
#         VIDEO = 'VD', 'Video'
#         LOCATION = 'LN', 'Location'

#     status = models.CharField(max_length=20,
#                               choices=Status.choices,
#                               default=Status.GALLERY)
#     title = models.CharField(max_length=155)
#     file = models.FileField(upload_to='media/files/resource', blank=True, null=True)
#     link = models.URLField(blank=True, null=True)
#     latitude = models.CharField(max_length=500, blank=True, null=True)
#     longitude = models.CharField(max_length=500, blank=True, null=True)


# class Location(models.Model):
#     latitude = models.CharField(max_length=500, blank=True, null=True)
#     longitude = models.CharField(max_length=500, blank=True, null=True)

#     def __str__(self):
#         return str(self.latitude) + " " + str(self.longitude)


# class File(models.Model):
#     file = models.FileField(upload_to='media/files/resource', blank=True, null=True)

#     def __str__(self):
#         return str(self.pk)


class Resource(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='resources')
    filter_category = models.ForeignKey(FilterCategories, on_delete=models.SET_NULL, null=True, related_name='resources')
    filters = models.ManyToManyField(Filters, blank=True, related_name='resources')
    period_filter = models.ForeignKey(PeriodFilter, on_delete=models.SET_NULL, null=True, related_name='resources')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images/resource', blank=True, null=True)
    content = models.TextField()
    statehood = models.BooleanField(default=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, related_name='resources')

    class Meta:
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'

    def __str__(self):
        return self.title


class Attributes(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True, related_name='attributes')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Contents(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True, related_name='contents')
    title = models.CharField(max_length=255)
    description = models.TextField()


class Gallery(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='galleries')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images/resource', blank=True, null=True)


class GalleryImages(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='media/images/resource')

    def __str__(self):
        return self.image.url


class File(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='files')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/files/resource', blank=True, null=True)


class FileFile(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='file_files')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='file_files')
    file = models.FileField(upload_to='media/files/resource')

    def __str__(self):
        return self.file.url


class Audio(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='audios')
    title = models.CharField(max_length=255)
    audio = models.FileField(upload_to='media/files/resource', blank=True, null=True)


class AudioFile(models.Model):
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, related_name='audio_files')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='audio_files')
    file = models.FileField(upload_to='media/files/resource')

    def __str__(self):
        return self.file.url


class VirtualReality(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='virtual_realities')
    title = models.CharField(max_length=255)
    audio = models.FileField(upload_to='media/files/resource', blank=True, null=True)


class VirtualRealityFile(models.Model):
    virtual_reality = models.ForeignKey(VirtualReality, on_delete=models.CASCADE, related_name='files')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='vr_files')
    file = models.FileField(upload_to='media/files/resource')

    def __str__(self):
        return self.file.url


class Video(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/files/resource', blank=True, null=True)
    link = models.URLField(max_length=500, null=True, blank=True)


class VideoFile(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='files')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='video_files')
    file = models.FileField(upload_to='media/files/resource')
    link = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.file.url


class Location(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='locations')
    title = models.CharField(max_length=255)
    latitude = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.CharField(max_length=500, blank=True, null=True)


class AddLocation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='additional_locations')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='additional_locations')
    latitude = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.CharField(max_length=500, blank=True, null=True)
