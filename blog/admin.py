from django.contrib import admin

#Importamos el modelo(clase) Post
from .models import Post

#Registramos el modelo para hacerlo visible
admin.site.register(Post)


