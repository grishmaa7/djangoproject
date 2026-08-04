from django.shortcuts import render

def home(request):
    number_list = {6,7,6,7}
    context = {'name': 'Grishma', 'age': 19, "numbers": number_list}
    return render(request, "teachers/home.html" , context)

