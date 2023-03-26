from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin , ExportActionModelAdmin
from modeltranslation.admin import TranslationAdmin
from .resources import *
from django.contrib.auth.models import User,Group

admin.site.unregister(User)
admin.site.unregister(Group)
@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display= ['name', 'telegram_id','language','phone','added']
    search_fields = ['name', 'telegram_id','language','phone']
    list_filter = ['language','added']
    list_per_page = 10
@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin,TranslationAdmin):
    list_display= ['name']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 10  
    resource_classes = [CategoryResource]  
@admin.register(SubCategory)
class SubCategoryAdmin(ExportActionModelAdmin,TranslationAdmin):
    list_display= ['name','category']
    search_fields = ['name','category__name']
    list_filter = ['name','category__name']
    list_per_page = 10 
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin,TranslationAdmin):
    list_display=['pic','name','category','subcategory']
    list_filter = ['discount','category__name','subcategory__name']
    list_per_page = 10 
    resource_classes = [ProductResource]
admin.site.register([Order,OrderItem])