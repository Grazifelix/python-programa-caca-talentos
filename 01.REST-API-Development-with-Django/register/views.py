from register.forms import RegisterForm
from django.shortcuts import render

# Create your views here.
def register(request): 
    success = False
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            success = True
            form.save()

    context = {
        'form': form,
        'success': success
    }
        
    return render(request, 'register.html', context)