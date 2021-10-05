from django.db import models
from .models import *

# Create your models here.
class CourseManager(models.Manager):
    def fields_validator(self, postData):
        errors = {}
        if len(postData['name'].strip()) < 5:
            errors['name_len'] = "Nombre del curso debe tener al menos 5 caracteres"
        return errors

class ItemManager(models.Manager):
    def fields_validator(self, postData):
        errors = {}
        if len(postData['description'].strip()) < 15:
            errors['description_len'] = "La descripción del curso debe tener al menos 15 caracteres"
        return errors


class Course(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
            return self.name  

class Item(models.Model):
    description = models.CharField(max_length=100, blank=False, null=False)
    creator = models.OneToOneField(Course, related_name="descrip_course", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()

    def __str__(self):
        return self.description
