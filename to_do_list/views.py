from django.shortcuts import render

list = []

def todolist(request):
    if request.method == 'POST':
        tache = request.POST.get('tache')
        if tache:
            list.append(tache)
            print("La tache a bien été ajoutée")
        else:
            print("Veuillez saisir une tache")
    return render(request, 'todolist.html', {'list': list})