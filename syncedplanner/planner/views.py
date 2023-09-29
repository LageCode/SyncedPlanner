from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EventCreationForm

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = EventCreationForm()
            print(form)
            return render(request, 'planner/index.html', {'user': request.user, 'form': form})
        elif request.method == 'POST':
            form = EventCreationForm(data=request.POST)
            if form.is_valid():
                new_event = form.save()
                messages.success(request, f'Appointment "{new_event.get_label()}" scheduled successfully.')
                return redirect('index')
            return render(request, 'planner/index.html', {'user': request.user, 'form': form})
    else:
        if request.method == 'POST':
            messages.error(request, f'Please sign in before scheduling an appointment.')
        return render(request, 'planner/index.html')

