from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
	form = TaskForm()
    #vérifier la méthode HTTP
	if request.method == "POST":
        #instancier le formulaire avec les données 
		form = TaskForm(request.POST)
        #tester la validité du formulaire
		if form.is_valid():
            #enregister les données
			form.save()
            #rediriger vers l'URL "index"
			return redirect("index")

	tasks = Task.objects.all()
	return render(request, "index.html", {"tasks": tasks,"task_form": form})





list = []

def todolist(request):
  
    if request.method == 'POST':
        task = request.POST.get('task')
        deadline = request.POST.get('deadline')
        priority = request.POST.get('priority')
        if task:
            list.append((task, deadline, priority))
            print("La tache a bien été ajoutée")
        else:
            error_message = "Veuillez saisir une tache"
            return render(request, 'todolist.html', {'list': list, 'error_message': error_message})
    return render(request, 'todolist.html', {'list': list})



def delete_item_to_do_list(request):
    if request.method == 'POST':
        task_index = int(request.POST.get('task_index'))
        list.pop(task_index)
    return redirect('todolist')




def update_item_to_do_list(request):
    if request.method == 'POST':
        task_index = int(request.POST.get('task_index'))
        task_name = request.POST.get('task')
        deadline = request.POST.get('deadline')
        priority = request.POST.get('priority')
        if task_name:
            list[task_index] = (task_name, deadline, priority)
            print("La tache a bien été mise à jour")
        else:
            print("Veuillez saisir une tache")
    return redirect('todolist')