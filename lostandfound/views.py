from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LostForm, FoundForm
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


@login_required
def lost(request):
    user = request.user

    #Lost.objects.all()
    if request.method == "POST":
        lost_form = LostForm(data=request.POST)
        if lost_form.is_valid():
            lost_item = lost_form.save(commit=False)
            lost_item.save()
    else:
        lost_form = LostForm()
    return render(request, 'lostandfound/lost.html', {'lost_form': lost_form,
                                                      'lost_object':Lost.objects.all().values()})



# @login_required
# def lost(request):
#     user = request.user
#     print(Lost.objects.all())
#     return render(request, 'lostandfound/lost.html', {})

def found(request):
    if request.method == "POST":
        found_form = FoundForm(data=request.POST)
        if found_form.is_valid():
            found_item = found_form.save(commit=False)
            found_item.save()
    else:
        found_form = FoundForm()
    return render(request, 'lostandfound/found.html', {'found_form': found_form,
                                                       'found_object': Found.objects.all().values()})

