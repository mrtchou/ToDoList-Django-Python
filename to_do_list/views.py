from django.shortcuts import render

list = []

def todolist(request):
    if request.method == 'POST':
        tache = request.POST.get('tache')
        deadline = request.POST.get('deadline')
        priority = request.POST.get('priority')
        if tache:
            list.append((tache, deadline, priority))
            print("La tache a bien été ajoutée")
        else:
            list.append(print("Veuillez saisir une tache"))
    return render(request, 'todolist.html', {'list': list})


