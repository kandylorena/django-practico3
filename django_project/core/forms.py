from django import forms
from django.core.validators import RegexValidator, EmailValidator


class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        min_length=2,
        required=True,
        label='Nombre completo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message='El nombre solo puede contener letras y espacios.',
            )
        ],
    )

    email = forms.EmailField(
        required=True,
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'}),
        validators=[
            EmailValidator(message='Ingresa un correo electrónico válido.'),
        ],
    )

    mensaje = forms.CharField(
        max_length=500,
        min_length=10,
        required=True,
        label='Mensaje',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escribe tu mensaje aquí...'}),
    )

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and nombre.strip().title() != nombre.strip():
            nombre = nombre.strip().title()
        return nombre

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        palabras_prohibidas = ['spam', 'publicidad', 'oferta']
        for palabra in palabras_prohibidas:
            if palabra in mensaje.lower():
                raise forms.ValidationError(f'El mensaje no puede contener la palabra "{palabra}".')
        return mensaje
