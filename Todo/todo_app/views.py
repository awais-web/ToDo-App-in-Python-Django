from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Tasks





def index(request):
    template =loader.get_template('index.html')
    TasksData = Tasks.objects.all().values()

    context = {
        'tasksData': TasksData
    }
    return HttpResponse(template.render(context, request))


def addTask(request):
    x = request.POST['taskName']
    Totable = Tasks(task=x)
    Totable.save()

    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    gettask = Tasks.objects.get(id=id)
    gettask.delete()

    return HttpResponseRedirect(reverse('index'))
