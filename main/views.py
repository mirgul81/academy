
from django.shortcuts import render
from .models import Academy, Manager, Mentor, Student


def index(request):
    academys = Academy.objects.all()
    context = {
        'academys': academys
    }
    return render(request, 'main/index.html', context)

def academy(request, pk):
    academys = Academy.objects.all()
    academy = Academy.objects.get(id=pk)
    managers = Manager.objects.filter(academy=academy)
    mentors = Mentor.objects.filter(academy=academy)
    context = {
        'academys': academys,
        'managers': managers,
        'mentors': mentors
    }
    return render(request, 'main/academy.html',context)

def manager(request, pk):
    managers = Manager.objects.all()
    manager = Manager.objects.get(id=pk)
    students = Student.objects.filter(manager=manager)
    context = {
        'managers': managers,
        'students': students,
        'manager': manager
    }
    return render(request, 'main/manager.html',context)

def mentor(request, pk):
    mentors = Mentor.objects.all()
    mentor = Mentor.objects.get(id=pk)
    students = Student.objects.filter(mentor=mentor)
    context = {
        'mentors': mentors,
        'students': students
    }
    return render(request, 'main/mentor.html',context)


def student(request, pk):
    students= Student.objects.all()
    student = Student.objects.get(id=pk)
    managers = Manager.objects.filter(mentor=mentor)
    mentors = Mentor.objects.filter(mentor=mentor)

    context = {

        'students': students,
        'managers': managers,
        'mentors': mentors
    }
    return render(request, 'main/student.html',context)
