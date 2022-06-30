from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


# Views can be considered routing objects that assign templates and other variables to a property (view).
#Renders the index template
def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == 'POST':
            if response.POST.get('save'):
                for item in ls.item_set.all():
                    if response.POST.get('c' + str(item.id)) \
                        == 'clicked':
                        item.complete = True
                    else:
                        item.complete = False

                        item.save()
            elif response.POST.get('newItem'):

                txt = response.POST.get('new')

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print ('invalid')

        return render(response, 'main/list.html', {'ls': ls})

    return render(response, 'main/home.html', {})

#Renders the home template

def home(response):
    return render(response, 'main/home.html', {})


# Renders to the create form template
#Creates a new to do list by checking if is a post request, then passes the inputted data into the ToDoList Model.
def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
            #saves ToDoList to a specific user
            response.user.todolist.add(t)

        return HttpResponseRedirect('/%i' % t.id)
    else:

        form = CreateNewList()

    return render(response, 'main/create.html', {'form': form})

#Renders view template
def view(response):
    return render(response, "main/view.html", {})