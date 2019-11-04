from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    class Media: #Se adapta a distintas pantallas(responsive)
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Page, PageAdmin)
