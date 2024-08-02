from django.contrib import admin
from base.models import Item, Category, Tag
from django.contrib.auth.models import Group
 
 
class TagInline(admin.TabularInline):
    model = Item.tags.through
 
class ItemAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['tags']

 
 
admin.site.register(Item,ItemAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.unregister(Group)