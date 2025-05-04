from django import forms

WORKOUT_OPTIONS = (
    ("1","Pull (Back,Biceps)"),
    ("2","Legs"),
    ("3","Full Body"),
)

class RegimentForm(forms.Form):
    regiment_field = forms.MultipleChoiceField(choices = WORKOUT_OPTIONS)
    