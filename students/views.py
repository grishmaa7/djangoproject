from django.shortcuts import HttpResponse, render
from django.views import View
from .models import Student
def hoome(request):
    return HttpResponse("Hewwwooooo, 'm grrrshma!")



def detail(request, id):
    return HttpResponse(
        f"You asked for student #{id}"
        )


def home(request):
    context ={'name': 'Grishma'}
    return render(request, 'home.html', context)


class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, i so prwetyyy")






def student_list(request):
    students = Student.objects.all()
    return render(request, "students/list.html", {"students": students})

