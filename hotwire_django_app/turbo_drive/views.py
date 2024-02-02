import http
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from hotwire_django_app.tasks.forms import TaskForm
from hotwire_django_app.tasks.models import Task

def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Task created successfully')
            return redirect(reverse('turbo-drive:task-list'))
        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        status = http.HTTPStatus.OK
        form = TaskForm()

    return render(request, 'turbo_drive/create.html', {'form': form}, status=status)


def list_view(request):
    object_list = Task.objects.all().order_by('-pk')

    context = {
        "object_list": object_list,
    }

    return render(request, 'turbo_drive/list.html', context)