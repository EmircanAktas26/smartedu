from django.contrib import admin
from . models import Course,Category,Tag

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available',)
    search_fields = ('name', 'descriptation')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}