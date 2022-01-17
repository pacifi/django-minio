from django.db import models


class Persona(models.Model):
    nombre = models.CharField(u"Nombre", max_length=50)
    foto = models.ImageField(u"Foto", upload_to="myapp/personas/fotos", blank=True, null=True)
    documento = models.FileField(u"Documento", upload_to=u"myapp/personal/documentos/", blank=True, null=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.nombre
