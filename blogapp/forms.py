from django import forms
from .models import Idea


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['texto']  # Los campos que el usuario pueda completar al agregar un comentario
        labels = {
            'texto': 'Idea'  # Personalizar las etiquetas de los campos
        }
        widgets = {
            'texto': forms.TextInput(attrs={'placeholder': "Escribe tus ideas y/o comentarios",
                                           # 'class' :"enteremail",
                                           #'name':"email",
                                           #'id':"subscribe-email",
                                           #'spellcheck':"false",
                                           #'type':"text"
                                           }),
        }
