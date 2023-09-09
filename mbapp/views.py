from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm,MessageUpdate

# Create your views here.


def index(request):
    messages = Message.objects.all()
    context = {'messages': messages}
    return render(request, 'home.html', context)

def list(request):
    messages = Message.objects.all()
    context = {'messages': messages}
    return render(request, 'message_list.html', context)
    

def detail(request, pk):
    messages = Message.objects.get(id=pk)
    context = {'message': messages}
    return render(request, 'message_detail.html', context)


def create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MessageForm()
    context = {'form': form}
    return render(request, 'message_create.html', context)


def edit(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == 'POST':
        form = MessageUpdate(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MessageUpdate(instance=message)
        context = {'form': form, 'message': message}
    return render(request, 'message_update.html', context)


def delete(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    context = {'message': message}
    return render(request, 'message_delete.html', context)






# class messagelistview(ListView):
#     model = Message
#     template_name = 'home.html'


# class messagedetailview(DetailView):
#     model = Message
#     template_name = 'message_detail.html'