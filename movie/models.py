from django.db import models
from django.shortcuts import reverse



class Settings(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/')
    facebook = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    vk = models.CharField(max_length=255, blank=True, null=True)
    ok = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.title 

    class Meta:
        verbose_name_plural = "Настройки"


class Contact(models.Model):
    phone1 = models.CharField(max_length=12, verbose_name="телефон №1")
    phone2 = models.CharField(max_length=12, verbose_name="телефон №2")
    address_link = models.CharField(max_length=100, verbose_name="link address", null=True)
    address = models.CharField(
        max_length=222,verbose_name="адрес",help_text="например: Ленина, 316, ​90 филиалов с. Новопокровка, Ысык-Атинский район Чуйская область 1 этаж")
    address_map = models.TextField(verbose_name="ссылка на местоположение")

    def __str__(self) -> str:
        return f"Контакты"
    
    class Meta:
        verbose_name_plural = 'Контакты'


class Actors(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО") 
    age = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='Фото')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("actor_detail", kwargs={"slug": self.name})
    
    
    class Meta:
        verbose_name_plural = "Актеры"

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
    v_rolyah = models.ManyToManyField(Actors, blank=True, related_name="film_actor")
    desc = models.TextField(blank=True, null=True)
    url_trailer = models.TextField(verbose_name="ссылка на трейлер", blank=True, null=True)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return f"{self.title} {self.draft}"
    
    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = 'Фильмы'


class News(models.Model):
    title = models.CharField(max_length=200)
    desc =models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='news/')
    genre = models.ForeignKey('CategoryNews', on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.title} | {self.genre}"

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.slug})
    

    class Meta:
        verbose_name_plural = "Новости"


class CategoryNews(models.Model):
    title = models.CharField(max_length=200, verbose_name="название категории")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Категории новостей"