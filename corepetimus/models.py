from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class PetimusType(models.Model):
    description = models.CharField(_('Descipción del tipo de Petimus'), max_length=100)

    def __str__(self):
        return self.description


class Petimus(models.Model):
    STATUS_CHOICES = (
        ('draft', _('Borrador')),
        ('published', _('Publicado')),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='petimus')
    title = models.CharField(_('Título Petimus'), max_length=100)
    description = models.CharField(_('Descipción del Petimus'), max_length=500)
    petimus_type = models.ForeignKey(PetimusType, on_delete=models.CASCADE, 
        related_name='petimus_type')
    country = models.CharField(_('Pais'), max_length=50)
    administrative = models.CharField(
        _('Provincia / comunidad autonoma'), max_length=100)
    city = models.CharField(_('Ciudad'), max_length=50)
    address = models.CharField(_('Dirección'), max_length=100)
    zip_code = models.CharField(_('Código postal'), max_length=15)
    #geoposition = models.CharField(max_length=100)
    solvitur_date = models.DateTimeField(blank=True, null=True)
    solvitur_description = models.CharField(max_length=500, blank=True, null=True)
    status = status = models.CharField(
        _('Estado'), max_length=10, choices=STATUS_CHOICES, default='published')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return _('Petimus {} en {} creada el {}').format(
            self.title, self.city, self.created)


# file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
def user_directory_path(instance, filename):
    # ej 20220812-222922
    date = datetime.now().strftime("%Y%m%d-%H%M%S")
    return 'u_{0}/{2}-{1}'.format(instance.petimus_id.user_id, filename, date)

class Image(models.Model):
    SOLVITUR_CHOICES = (
        (False, _('No')),
        (True, _('Si')),
    )
    image = models.ImageField(upload_to=user_directory_path)
    # url = models.URLField(blank=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    solvitur = models.BooleanField(
        _('Restuelto Si/No'), max_length=3, choices=SOLVITUR_CHOICES, default=False)
    petimus = models.ForeignKey(Petimus, on_delete=models.CASCADE, related_name='petimus_images')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comment')
    petimus = models.ForeignKey(
        Petimus, on_delete=models.CASCADE, related_name='petimus_comment')
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return _('Comentario: {} . Usuario: {} . Petimus {}').format(
            self.id, self.user, self.petimus_id.title)

class Notification(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_notification')
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    view = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return _('Notificación: {} del usuario {} leida: {}').format(
            self.id, self.user, self.view)
    