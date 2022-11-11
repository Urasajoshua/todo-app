from django.shortcuts import render ,redirect
from . models import Mytodo
from . form import Todoform

def index(request):
    tasks=Mytodo.objects.all()
    form = Todoform()
    if request.method == 'POST':
        form = Todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=Todoform()
    return render(request,'index.html',{'tasks':tasks,'form':form})


def deleteItem(request,pk):
    tasks=Mytodo.objects.get(id=pk)
    tasks.delete()
    return redirect('index')

def updateItem(request , pk):
    tasks=Mytodo.objects.get(id=pk)
    updateForm=Todoform(instance=tasks)
    if request.method == 'POST':
        updateForm=Todoform(request.POST , instance=tasks)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('index')
    return render(request,'update.html',{'tasks':tasks,'updateForm':updateForm})

