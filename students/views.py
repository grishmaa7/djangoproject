from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Hewwwooooo, 'm grrrshma!")



def detail(request, id):
    return HttpResponse(f"You asked for student #{id}")


