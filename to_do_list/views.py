from django.shortcuts import render





def todolist(request):
    list = []
    if request.method == 'POST':
        tache = request.POST.get('tache')
        if tache:
            list.append(tache)
            print("La tache a bien été ajoutée")
        else:
            print("Veuillez saisir une tache")
    return render(request, 'todolist.html', {'list': list})
