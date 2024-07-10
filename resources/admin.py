from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, FilterCategories, PeriodFilter, Filters,  Resource, Province, File, Location

admin.site.register(Category)
admin.site.register(FilterCategories)
admin.site.register(PeriodFilter)
admin.site.register(Filters)
admin.site.register(File)
admin.site.register(Location)
admin.site.register(Province)



@admin.register(Resource)
class ResourseModelAdmin(admin.ModelAdmin):
    list_display = ["title", "category"]

    class Media:
        js = (
            "dropdown.js",
            "https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js",
        )
