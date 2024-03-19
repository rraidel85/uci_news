from django.db import models
from usuarios.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Temáticas'
        verbose_name_plural = 'Temáticas'
        
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    url = models.CharField(max_length=255, verbose_name='URL')
    pub_date = models.DateField(verbose_name='Fecha de publicación')
    source = models.CharField(max_length=255, verbose_name='Fuente')
    gender = models.CharField(max_length=255, verbose_name='Género')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='news/', verbose_name='Imagen')
    ideological_stance = models.CharField(max_length=255, verbose_name='Postura ideológica')
    descriptor = models.CharField(max_length=255, verbose_name='Descriptor')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    authors = models.ManyToManyField(CustomUser, related_name='authors', verbose_name='Autores')

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        
    def __str__(self):
        return self.title
