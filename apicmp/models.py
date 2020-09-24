from django.db import models

class Grupo(models.Model):
    numeral = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return '{}-{}'.format(self.numeral, self.nombre)        

    class Meta:
        verbose_name_plural = "Grupos"
        ordering = ['numeral']
    
        
class Area(models.Model):
    numeral = models.CharField(max_length=10) 
    nombre = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo, related_name='areas', blank=True, null=True, on_delete= models.CASCADE)

    class Meta:
        verbose_name_plural = "Areas"
        ordering = ['numeral']


    def __str__(self):
        return '{}'.format(self.id)
    

class Programa(models.Model):
    nombre = models.CharField(max_length=10)
    class Meta:
        verbose_name_plural = "Programas"
        ordering = ['id']

    def __str__(self):
        return '{}-{}'.format(self.id, self.nombre)


class Peso(models.Model):
    min = models.IntegerField()
    max = models.IntegerField()
    area = models.ForeignKey(Area, blank=True, null=True, on_delete=models.CASCADE)
    programa = models.ForeignKey(Programa, related_name='pesos', blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Pesos"
        ordering = ['id']

    def __str__(self):
        return '{}-{}-{}-{}'.format(self.area, self.min, self.max, self.programa)


class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre    

    class Meta:
        verbose_name_plural = "Paises"
        ordering = ['id']

class Universidad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Universidades"
    def __str__(self):
        return self.nombre

class ProgramaU(models.Model):
    nombre = models.CharField(max_length=100)
    universidad = models.ForeignKey(Universidad, blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "ProgramasU"
        ordering = ['id']

    def __str__(self):
        return '{}-{}'.format(self.nombre, self.universidad)

class PesoU(models.Model):
    min = models.IntegerField()
    max = models.IntegerField()
    area = models.ForeignKey(Area, blank=True, null=True, on_delete=models.CASCADE)    
    programau = models.ForeignKey(ProgramaU, blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "PesosU"

    def __str__(self):
        return '{}-{}'.format(self.min, self.max)
