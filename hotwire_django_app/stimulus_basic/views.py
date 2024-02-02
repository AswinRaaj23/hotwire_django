import http
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from hotwire_django_app.tasks.forms import TaskForm
from hotwire_django_app.tasks.models import Task
from django.shortcuts import render

def counter_view(request):
    return render(request, 'stimulus_basic/counter.html')

def create_view(request):                         # new
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Task created successfully')
            return redirect(reverse('stimulus-basic:task-list'))

        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        status = http.HTTPStatus.OK
        form = TaskForm()

    return render(request, 'stimulus_basic/create_page.html', {'form': form}, status=status)


def list_view(request):                           # new
    object_list = Task.objects.all().order_by('-pk')

    context = {
        "object_list": object_list,
    }

    return render(request, 'stimulus_basic/list_page.html', context)