from django.shortcuts import render, redirect

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
            list.append(print("Veuillez saisir une tache"))
    return render(request, 'todolist.html', {'list': list})



def delete_last_item_to_do_list(request):
    if request.method == 'POST':
        task_index = int(request.POST.get('task_index'))
        
        list.pop(task_index)
    return redirect('todolist')
