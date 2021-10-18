from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Addition, Subtraction, Multiplication, Division
from .models import Result
# Create your views here.



# home/-home page, calculator/-calculator page, info/-information about math and its brances, videos/-videos with math
# /calculator/additions

def home(response):
    return render(response, 'mainsite/index.html',{})


# KINDA BROKEN DOWN THERE
def calculator(response):
    if response.method == "POST":
        form1 = Addition(response.POST)
        form2 = Subtraction(response.POST)
        form3 = Multiplication(response.POST)
        form4 = Division(response.POST)
        if form1.is_valid() and response.POST.get('save1'):
            add1 = form1.cleaned_data['Addition1']
            add2 = form1.cleaned_data['Addition2']
            add3 = add1 + add2
            resultadd = Result.objects.get(name="resultadd")
            resultadd.value = add3
            resultadd.save()
        elif form2.is_valid() and response.POST.get('save2'):
            sub1 = form2.cleaned_data['Subtraction1']
            sub2 = form2.cleaned_data['Subtraction2']
            sub3 = float(sub1) - float(sub2)
            setattr(resultsub, "value", sub3)
            resultsub.save()
        elif form3.is_valid() and response.POST.get('save3'):
            multi1 = form3.cleaned_data['Multiplication1']
            multi2 = form3.cleaned_data['Multiplication2']
            multi3 = float(multi1) * float(multi2)
            setattr(resultmulti, "value", multi3)
            resultmulti.save()
        elif form4.is_valid() and response.POST.get('save4'):
            div1 = form4.cleaned_data['Division1']
            div2 = form4.cleaned_data['Division2']
            div3 = float(div1) / float(div2)
            setattr(resultdiv, "value", div3)
            resultdiv.save()
    else:
        form1 = Addition()
        form2 = Subtraction()
        form3 = Multiplication()
        form4 = Division()
    return render(response, 'mainsite/calculator.html', {"form11":form1, "form22":form2, "form33":form3, "form44":form4})


def results(response):
    resultadd = Result.objects.get(name="resultadd")
    resultsub = Result.objects.get(name="resultsub")
    resultmulti = Result.objects.get(name="resultmulti")
    resultdiv = Result.objects.get(name="resultdiv")
    return render(response, 'mainsite/results.html', {"resultadd":resultadd, "resultmulti":resultmulti, "resultdiv":resultdiv, "resultsub":resultsub})

def info(response):
    return render(response, 'mainsite/info.html', {})


def videos(response):
    return render(response, 'mainsite/videos.html', {})

def author(response):
    return render(response, 'mainsite/author.html', {})
