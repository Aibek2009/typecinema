
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from movie.views import homepage, NewsDetailView, contact, MovieDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('contact/', contact, name='contact'),
    path('news/<str:slug>/', NewsDetailView.as_view(), name="news_detail"),
    path('movie/<str:slug>/', MovieDetailView.as_view(), name="movie_detail")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)