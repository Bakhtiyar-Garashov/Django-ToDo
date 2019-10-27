from django.shortcuts import render, redirect
from .models import Entry


# Create your views here.
def index(request):
    entries = Entry.objects.all()
    context = {
        "entries": entries
    }
    return render(request, "index.html", context=context)


def add_entry(request):
    title = request.POST['title']
    content = request.POST['content']
    new_entry = Entry(title=title, content=content)
    new_entry.save()
    return redirect(index)
