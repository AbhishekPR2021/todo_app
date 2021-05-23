from django import forms

from todo_app.models import todo


class Todo_update(forms.ModelForm):
    class Meta:
        model=todo
        fields=['item','priority','date']
