from django import forms


class HomeForm(forms.Form):
    location = forms.CharField()
    OPTIONS = (("HAPPY", "Happy"), ("ADVENTUROUS", "Adventurous"), ("CHILL", "Chill"), ("WOW", "Wow"))
    personalities = forms.CheckboxSelectMultiple(choices=OPTIONS)
    # checkboxes = forms.CheckboxSelectMultiple()

    
