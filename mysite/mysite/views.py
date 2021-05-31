#Created by Swapnil Shah 12:36, 31/05/21
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Swapnil','place':'Mars'}
    return  render(request,'index2.html',params)
    # return HttpResponse("<h1>Hello</h1>")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removePunc',"off")
    fullcaps = request.POST.get('fullcaps',"off")
    countchar = request.POST.get('countchar',"off")
    removenewline = request.POST.get('removenewline',"off")
    purpose = ""
    analyzed = ""

    if removepunc == "on":
        purpose = purpose+"Remove Punctuations"
        #Analyze text
        punctuations = '''!,.;'"!(){}[]:-_\<>?@#%^*~`'''
        for c in djtext:
            if c not in punctuations:
                analyzed = analyzed+c



    if fullcaps == "on":
        if purpose!="":
            purpose = purpose+", UPPERCASE"
        else:
            purpose = "UPPERCASE"
            analyzed = str(djtext)
        analyzed = analyzed.upper()

    charcount = ""
    if countchar == "on":
        if purpose!="":
            purpose = purpose+", Count Characters"
        else:
            purpose = "Count Characters"
            analyzed = str(djtext)

        charcount = "Total Character count : " + str(len(analyzed))

    if removenewline == "on":
        if purpose != "":
            purpose = purpose + ", Remove New Line"
        else:
            purpose = "Remove New Line"
            analyzed = str(djtext)
        print(analyzed.count("\n"))
        analyzed = analyzed.replace("\n","")
        print(analyzed.count("\n"))


    params = {'purpose': purpose, 'analyzed_text': analyzed, 'charcount':charcount}

    return render(request, 'analyze2.html', params)
    return HttpResponse("No option selected")

def capitalizeFirst(request):
    return HttpResponse("capitalize First")



def contactUs(request):
    return render(request,'contactus.html')
    # return HttpResponse("<h1>Hello</h1>")

def aboutUs(request):
    return render(request,'aboutus.html')
    # return HttpResponse("<h1>Hello</h1>")