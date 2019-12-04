from django.db import models
from django.utils import timezone

#En esta carpeta se definen los models, los posteos basicamente
#Se trabaja con POO, cada model es un objeto


class Post(models.Model):
    #   ATENCION
    #   Estos atributos que defino dentro de mi objeto, son en si, atributos
    #   A la hora de traer la informacion de mi BD, no debo definir el tipo y limite de la cantidad con SQL
    #   El mismo framework(DJANGO) lo hace por mi en esta parte del codigo
#ATRIBUTOS

    #   Definimos la relacion con otro modelo
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    #El titulo tiene un tope de 200 caracteres
    title = models.CharField(max_length=200)
    
    #El cuerpo del posteo tiene cantidad ilimitada de caracteres
    text = models.TextField()

    #Fecha de creacion y publicacion del posteo
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


#METODOS
    #Self seria this en java, hace referencia a atributos dentro de mi objeto
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #Devuelve el titulo del post
    def __str__(self):
        return self.title