from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    try:
        contact = Contact.objects.get(name='Yuriy', last_name='Lyashko')
    except:
        name, last_name, date_of_birth, bio, email, jabber, skype, other_contacts = Contact.get_contact_data()
        contact = Contact(name=name, last_name=last_name, date_of_birth=date_of_birth, bio=bio, email=email,
                          jabber=jabber, skype=skype, other_contacts=other_contacts
                          )
        contact.save()
    finally:
        contact.bio, contact.other_contacts = eval(contact.bio), eval(contact.other_contacts)
        return render(request, 'index.html', {'contact': contact})