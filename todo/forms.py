from django import forms 

class TodoForm(forms.Form):
    text = forms.CharField(max_length=160,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'e.g Delete junk files', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))