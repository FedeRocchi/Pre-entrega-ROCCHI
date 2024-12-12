from django.db import models


class User_register(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    dni = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.email} - {self.dni}'
    

    


