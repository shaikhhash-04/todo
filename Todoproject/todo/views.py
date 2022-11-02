from django.shortcuts import render,redirect
from todo.models import Task
# Create your views here.
def add(request):
    if(request.method=="POST"):
        heading = request.POST['heading']
        detail = request.POST['detail']
        date = request.POST['date']

        print(heading)
        print(detail)
        print(date)

        insert_data = Task.objects.create(heading = heading, detail = detail, date= date)
        insert_data.save()
        return redirect("/")
    return render(request,'todo/add.html')


def index(request):
     content ={}
     content['data']=Task.objects.filter(is_deleted="n")
     return render(request,'todo/index.html',content)

def delete(request,tid):
    record_to_deleted = Task.objects.filter(id=tid)
    #record_to_deleted.delete()
    record_to_deleted.update(is_deleted="y")
    return redirect("/")

def update(request,tid):
    if(request.method=="POST"):
        heading = request.POST['heading']
        detail = request.POST['detail']
        date = request.POST['date']
        record_to_update=Task.objects.filter(id=tid)
        record_to_update.update(heading=heading,detail=detail,date=date)
        return redirect("/")
    else:
        content={}
        content['data']=Task.objects.get(id=tid)
        return render(request,'todo/update.html',content)
