from django import forms
from .models import Task


class CustomDateWidget(forms.widgets.DateInput):

    template_name = 'form/flatpickr_date.html'


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("title", "due_date")
        widgets = {
            'due_date': CustomDateWidget(),
        }