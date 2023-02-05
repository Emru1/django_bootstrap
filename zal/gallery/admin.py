from django.contrib import admin

from gallery.models import Gallery, Image, GalleryComment, ImageComment

# Register your models here.

admin.site.register(Gallery)
admin.site.register(Image)
admin.site.register(GalleryComment)
admin.site.register(ImageComment)
