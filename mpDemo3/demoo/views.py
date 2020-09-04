from django.shortcuts import render
from django.http import HttpResponse
from demoo.forms import RegisterForm
# Create your views here.
def homee(req):
    return render(req,"demo/home.html",{})


def Register(req):
        context = {}
        form = RegisterForm(req.GET or None)
        if form.is_valid():
            form.save()
        context['Form'] = form
        # regobj = registration.objects.all()
       # return render(req, "demo/register.html", context)
        return render(req,'demo/register.html',{'form':form})






