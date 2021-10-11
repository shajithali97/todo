from django.shortcuts import redirect, render
from . models import Task
from . forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

class TaskListView(ListView):
    model=Task
    template_name='index.html'
    context_object_name='task'

class TaskDetailView(DetailView):
    model=Task
    template_name='cbv_detail.html'
    context_object_name='i'

class TaskUpdateView(UpdateView):
    model=Task
    template_name='cbv_update.html'
    context_object_name='task'
    fields=('task_name','task_priority','task_date')
    def get_success_url(self):
        return reverse_lazy('todo_app:cbv_detail',kwargs={'pk':self.object.id,})

class TaskDeleteView(DeleteView):
    model=Task
    template_name="delete.html"
    success_url=reverse_lazy('todo_app:cbv_home')


# Create your views here.
def home(request):


    task=Task.objects.all()
    
    if request.method =="POST":

        task_name=request.POST.get('task_name')
        task_priority=request.POST.get('task_priority')
        task_date=request.POST.get('task_date')
        t=Task(task_name=task_name,task_priority=task_priority,task_date=task_date)
        t.save()
        print(f"{task_name}--{task_date}--{task_priority}")
        return redirect('/')

    return render(request,'index.html',{'task':task})



def update(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})

def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})