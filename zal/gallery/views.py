from django.shortcuts import render, get_object_or_404
from django.views import View

from gallery.models import Gallery, Image


class IndexView(View):
    def get(self, request):
        gals = Gallery.objects.all()
        scope = {
            'galleries': gals,
        }

        return render(request, 'index.html', scope)


class GalleryView(View):
    def get(self, request, id):
        gallery: Gallery = get_object_or_404(Gallery, id=id)
        images = gallery.images_rel.all()
        comments = gallery.comments_rel.all()
        scope = {
            'gallery': gallery,
            'images': [images[x:x+3] for x in range(0, len(images), 3)],
            'comments': [comments[x:x+3] for x in range(0, len(comments), 3)],
        }

        return render(request, 'gallery.html', scope)


class ImageView(View):
    def get(self, request, id):
        image: Image = get_object_or_404(Image, id=id)
        gallery: Gallery = image.gallery
        comments = image.comments_rel.all()
        scope = {
            'gallery': gallery,
            'image': image,
            'comments': [comments[x:x+3] for x in range(0, len(comments), 3)],
        }

        return render(request, 'image.html', scope)
