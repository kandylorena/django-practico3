from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request, 'core/index.html')


def contacto(request):
    context = {'form': ContactForm()}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            context['success'] = f'Mensaje enviado correctamente por {nombre}. Te contactaremos a {email}.'
            context['form'] = ContactForm()
        else:
            context['form'] = form
    return render(request, 'core/contacto.html', context)
