from django import forms

class divsForm(forms.Form):
	text = forms.CharField(max_length=40, 
		widget=forms.TextInput(
			attrs={'class' : 'form-control', 'placeholder' : 'Enter divs e.g. Delete junk files', 'aria-label' : 'divs', 'aria-describedby' : 'add-btn'}))
