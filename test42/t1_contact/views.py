from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    t = Contact()
    print(t.name)
    t.bio, t.other_contacts = dict(t.bio), dict(t.other_contacts)
    return render(request, 'index.html', {'t': t})