from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import ToDoItem

# Create your views here.
'''def hello(request):
    return HttpResponse('Hi, Nice to meet you')

def doappView(request):
    return render(request, 'base.html')'''


def doappView(request):
    all_item = ToDoItem.objects.all()
    return render(request, 'todo.html', {'items_display':all_item})

def addTodo(request):
    user_item = ToDoItem(content = request.POST['content'])
    user_item.save()
    return HttpResponseRedirect('/')

def deleteTodo(request, items_id):
    item_delete = ToDoItem.objects.get(id= items_id)
    item_delete.delete()
    return HttpResponseRedirect('/')
