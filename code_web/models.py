from django.db import models

class usuarios_registrados(models.Model):
    nombre = models.CharField(max_length=70)
    email = models.EmailField()
    comentarios = models.TextField()
    
    class Meta:
        indexes = [
            models.Index(fields=["nombre",]),
            models.Index(fields=["email",]),
            models.Index(fields=["comentarios",]),
        ]
    
    def __str__(self):
        return self.nombre