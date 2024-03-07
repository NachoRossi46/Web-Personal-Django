from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Titulo") # max_length=100 -> longitud máxima del campo
    description = models.TextField(verbose_name = "Descripcion")
    image = models.ImageField(verbose_name = "Imagen", upload_to="projects") # upload_to="projects" -> carpeta donde se guardan las imagenes
    link = models.URLField(null=True, blank=True, verbose_name = "Direccion web") # null=True -> campo puede ser nulo, blank=True -> campo puede estar vacio
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion") # auto_now_add=True -> cuando se crea el objeto se guarda la fecha y hora
    uptaded = models.DateTimeField(auto_now=True, verbose_name = "Fecha de actualizacion") # auto_now=True -> cuando se actualiza el objeto se guarda la fecha y hora

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] # Ordena los proyectos por fecha de creación de forma descendente, es decir primero los mas nuevos
        
    def __str__(self):
        return self.title
