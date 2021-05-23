from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from todo_app.forms import Todo_update
from todo_app.models import todo


#
#
# class TaskListView(ListView):
#     model = todo
#     template_name = 'home.html'
#     context_object_name = 'k'
#
#
# class TaskDetailView(DetailView):
#     model = todo
#     template_name = 'details.html'
#     context_object_name = 'obj1'
#
# class TaskUpdateView(UpdateView):
#     model = todo
#     template_name = 'edit.html'
#     context_object_name = 'obj'
#     fields = ['item','priority','date']
#     def get_success_url(self):
#         return reverse_lazy('cbvhome',kwargs={'pk':self.object.id})
#
# class TaskDeleteView(DeleteView):
#     model = todo
#     template_name = 'delete.html'
#     success_url = reverse_lazy('cbvhome')
#
#
#
#




def home(request):
    obj = todo.objects.all()

    if request.method=='POST':

        item=request.POST.get('item')
        pri=request.POST.get('pri')
        date=request.POST.get('date')
        s=todo(item=item,priority=pri,date=date)
        s.save()
    return render(request,'home.html',{'k':obj})
def details(request,id):
    obj1=todo.objects.get(id=id)
    return render(request,'details.html',{'obj1':obj1})


def delete(request,id):
    obj=todo.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    obj=todo.objects.get(id=id)
    form=Todo_update(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'obj':obj,'form':form})