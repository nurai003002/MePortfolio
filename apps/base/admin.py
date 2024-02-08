from django.contrib import admin

from apps.base import models
# Register your models here.

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ( 'title','created_at','image', 'description')
    list_filter = ( 'title','created_at','image','description' )

@admin.register(models.Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ( 'review','name','work','image')
    list_filter = ( 'review','name','work','image' )

@admin.register(models.Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ( 'image',)
    list_filter = ( 'image', )

@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video', 'image')
    list_filter = ('video', 'image')

@admin.register(models.Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'work', 'image')
    list_filter = ('name', 'logo', 'work', 'image')

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')
    list_filter = ('title', 'image', 'description')

@admin.register(models.Catigory)
class CatigoryAdmin(admin.ModelAdmin):
    list_display = ('catigory_amount',)
    list_filter = ('catigory_amount', )

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_filter = ('title', 'image')

class SkillsPercentInline(admin.TabularInline):
    model = models.SkillsPercent
    extra = 1

class SkillsPercentAdmin(admin.ModelAdmin):
    
    inlines = [SkillsPercentInline]

admin.site.register(models.Contacts)
admin.site.register(models.Skills, SkillsPercentAdmin)