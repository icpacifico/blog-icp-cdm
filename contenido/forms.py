from django import forms
from .models import Comentario, Respuesta

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor','texto']  # Los campos que deseas que el usuario pueda completar al agregar un comentario
        labels = {
            'autor': 'Autor',
            'texto': 'Comentario'  # Puedes personalizar las etiquetas de los campos si lo deseas
        }
        widgets = {
            'autor': forms.TextInput(attrs={'rows': 4, 'placeholder': 'Autor'}),
            'texto': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu comentario aquí'})  # Personaliza el widget del campo de texto
        }

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['autor','texto']  # Los campos que deseas que el usuario pueda completar al agregar una respuesta
        labels = {
            'autor': 'Autor',
            'texto': 'Respuesta'  # Puedes personalizar las etiquetas de los campos si lo deseas
        }
        widgets = {
            'autor': forms.TextInput(attrs={'rows': 4, 'placeholder': 'Autor'}),
            'texto': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu respuesta aquí'})
            # Personaliza el widget del campo de texto
        }
