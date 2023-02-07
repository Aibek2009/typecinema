from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    draft = models.BooleanField(verbose_name="фильм вышел", default=False)
    image = models.ImageField(upload_to='movie/')
    country = models.CharField(max_length=100)
    year = models.CharField(max_length=100, blank=True, null=True)
    slogan = models.CharField(max_length=100, blank=True, null=True)
    rejissr = models.CharField(max_length=100, blank=True, null=True)
    ssenary = models.CharField(max_length=100, blank=True, null=True)
    producer = models.CharField(max_length=100, blank=True, null=True)
    janr = models.CharField(max_length=100, blank=True, null=True)
    v_rolyah = models.CharField(max_length=100, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    url_trailer = models.CharField(max_length=100,verbose_name="ссылка на трейлер", blank=True, null=True)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return f"{self.title} {self.draft}"
    
    class Meta:
        verbose_name_plural = 'Фильмы'


