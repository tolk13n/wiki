from django.shortcuts import redirect, render
from django import forms
from django.core import validators
from django.http import HttpResponse  #   delite!!!
from . import util
import random
import markdown2



class NewPageForm(forms.Form):
    title = forms.CharField(label='title', validators=[validators.validate_slug], error_messages={'invalid': 'Неприйнятна назва. Будьласка використовуйте лише букви або цифри'}, widget=forms.TextInput(attrs={'size': '100%', }))
    content =  forms.CharField(label='content', widget=forms.Textarea)
    message = "asdfffffffff"


def index(request):
    if request.method == "POST":
        return HttpResponse("Поиск")
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def page(request, name):
    return render(request, "encyclopedia/page.html", {
        "name": name,
        "entries": markdown2.markdown(util.get_entry(name))
    })

def search(request):
    if request.method == "POST":
        text = request.POST
        question =text.get("q")

        if util.get_entry(question):
           return redirect( "/wiki/"+ question)
        else:
            answers = [i for i in util.list_entries() if question.lower() in i.lower()]
        return render(request, "encyclopedia/search.html", {
            "answers": answers
        })
    else:
        return HttpResponse("*******************")

def new(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title in util.list_entries():
                return render(request, "encyclopedia/new.html", {
                "form":form , "error1":title
                })

            util.save_entry(title, content)
            redirect( "/wiki/"+ title)
        return render(request, "encyclopedia/new.html", {
        "form":form
        })
    else:
        return render(request, "encyclopedia/new.html", {
        "form":NewPageForm()
        })

def edit(request, name):

        if request.method == "POST":
            form = request.POST
            title = name
            content = form.get("content")
            util.save_entry(title, content)
            return redirect( "/wiki/"+ title) 
        else:
            return render(request, "encyclopedia/edit.html", {
            "name": name,
            "entries": util.get_entry(name)
            })

def rnd(request):
        choice1 = random.choice(util.list_entries())
        return redirect( "/wiki/"+ choice1)        #  page(request, choice1)

