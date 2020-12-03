from django.shortcuts import render,redirect

from .models import *
from .forms import *

def accueil (request):
	text1= "Bienvenue sur notre cite web d'aviation"
	text2= "pour regarder les evenement "
	

	return render(request, "accueil.html", locals())


def event(request):
	events_form = eventsForm(request.POST, request.FILES)
	if(request.method == 'POST'):
		if(events_form.is_valid()):
			events_form.save()
			return redirect(listevents)
	events_form = eventsForm()

	return render(request, "forms.html", locals())

def contact(request):
	contact_form = contactForm(request.POST or None)
	if (request.method == 'POST'):
		if(contact_form.is_valid()):
			contact_form.save()

	contact_form = contactForm()

	return render(request, "forms.html", locals())




def paiement(request):
	text1="via lumicash" 
	number="68235685"
	text2="via ecocash" 
	number2="72456078"

	paiement_form=paiementForm(request.POST or None)
	if(request.method == 'POST'):
		if(paiement_form.is_valid()):

			paiement_form.save()

	paiement_form=paiementForm()
	return render(request,"forms.html",locals())


def listevents(request):
	listes = events.objects.all()
	return render(request,"listevents.html", locals())

def delete(request,id):
	event= events.objects.get(id=id)
	event.delete()
	return redirect(listevents)
	


