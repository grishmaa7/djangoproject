from django.shortcuts import HttpResponse, render
from django.views import View

def hoome(request):
    return HttpResponse("Hewwwooooo, 'm grrrshma!")



def detail(request, id):
    return HttpResponse(
        f"You asked for student #{id}"
        )


def hoome(request):
    context ={'name': 'Grishma'}
    return render(request, 'hoome.html', context)


class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, i so prwetyyy")


def student_list(request):
    students = ["Grishma", "Khusbu", "Nico"]
    return render(request, "students.html", {"students": students})


