from django.urls import path

from gallery.views import IndexView, GalleryView, ImageView


urlpatterns = (
    path('index/', IndexView.as_view()),
    path('gallery/<str:id>/', GalleryView.as_view()),
    path('image/<str:id>/', ImageView.as_view()),
)
