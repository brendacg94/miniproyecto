from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombres', max_length = 255, blank = False, null = False)
    last_name = models.CharField('Apellidos', max_length = 255, blank = False, null = False)
    email = models.EmailField('Correo electrónico', max_length = 255, blank = False, null = False)
    address = models.CharField('Dirección', max_length = 255, blank = False, null = False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.last_name}'



    

