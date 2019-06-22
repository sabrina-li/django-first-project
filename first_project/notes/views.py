from django.shortcuts import render, get_object_or_404
# from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse 

from .models import Notes

# Create your views here.

def detail(request, note_id):
    # return HttpResponse("You're looking at note %s." % note_id)
    note = Notes.objects.get(id=note_id)
    print("="*10)
    print(note.get_pub_date())
    context = {
        'note_id':note_id,
        'note_text':note,
        'pub_date':note.get_pub_date()
    }
    return render(request,'notes/detail.html',context)


def index(request):
    all_notes = Notes.objects.order_by('-pub_date')[:5]
    # output = '<br> '.join([n.note_text for n in all_notes])
    # template = loader.get_template('notes/index.html')
    context = {
        'all_notes': all_notes,
    }
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    return render(request, 'notes/index.html', context)


def add(request):
    return render(request, 'notes/add.html')