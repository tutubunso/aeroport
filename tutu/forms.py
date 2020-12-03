from django import forms
from .models import *


class eventsForm(forms.ModelForm):

	class Meta:
		model = events
		fields = '__all__'

class contactForm(forms.ModelForm):

	class Meta:
		model = contact
		fields = '__all__'

class paiementForm(forms.ModelForm):

	class Meta:
		model = paiement
		fields = '__all__'