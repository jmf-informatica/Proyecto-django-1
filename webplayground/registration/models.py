from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

# Se recupera el avatar guardado, se elimina y se retorna el objeto actual ( el nuevo avatar ) con su nombre, guardandolo en el fichero profiles/
def custom_upload_to(instance,filename):
    old_instance=Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link=models.URLField(max_length=200,null=True,blank=True)

#Esta función crea un perfil automaticamente en el caso que un usuario se registre y nunca acceda, ya que al no acceder no se crearia el perfil.
@receiver(post_save, sender=User) # Se ejecuta despues de guardar
def confirm_profile_exists(sender, instance,**kwargs): #Función para confirmar que el perfil siempre exista.
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance) #Si no existe lo crea
        print('Se ha creado un usuario y su perfil')




