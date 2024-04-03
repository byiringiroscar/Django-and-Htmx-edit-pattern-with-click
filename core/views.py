from django.shortcuts import render, get_object_or_404
from core.models import Student
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    context = {}
    return render(request, 'core/index.html', context)

def students(request):
    students = Student.objects.all()
    paginator = Paginator(students, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }

    if request.htmx:
        return render(request, 'core/partials/list.html', context)
    return render(request, 'core/index.html', context)



def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student
    }
    return render(request, 'core/student.html', context)