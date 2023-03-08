from django.shortcuts import render

list = []

def recuperation_saisi(request):
    tache = input("une tache a saisirr : ")
    if tache != "" or None or 0:
        list.append(tache)
        print("la tache a bien été ajouté ")
    else:
        print("veuillez saisir une tache")
    return render(request, 'todolist.html')
    

while True:
    recuperation_saisi()
    print(list)