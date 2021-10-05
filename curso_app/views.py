from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def root(request):
    course= Course.objects.all()
    description = Item.objects.all()
    context = {
        'courses': course,
        'descriptions': description,
    }

    return render(request, 'curso_app/add.html', context)

def create(request):
    if request.method == 'GET':
        return redirect('/') 
    else:
        if request.method == 'POST':
            errors = Course.objects.fields_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                    return redirect('/')
            errors = Item.objects.fields_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                    return redirect('/')
            else:         
                course = request.POST['name'] 
                description = request.POST['description']     
                obj_course = Course.objects.create(name=course)
                obj_descrip= Item.objects.create(description=description, creator=obj_course)
                obj_course.save()
                obj_descrip.save()
                messages.success(request, "Curso registrado con éxito")

            return redirect('root')
        
def info_course(request, course_id):
    course= Course.objects.get(id=course_id)
    context = {
        'course': course,
    }
    return render(request, 'curso_app/delete.html', context) 

def delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('/')