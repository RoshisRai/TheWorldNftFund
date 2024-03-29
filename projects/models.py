from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
# Create your models here.
class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(default='')
    sub_title = models.TextField()
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="projects/")
    project_content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

@receiver(post_delete, sender=Project)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.photo.delete(save=False)
    except:
        pass

@receiver(pre_save, sender=Project)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).photo.path
        try:
            new_img = instance.image.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass