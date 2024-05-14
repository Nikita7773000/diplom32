from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book, Grade, Author
from .forms import GradeForm, RegisterForm


def main(request):
    return render(request, 'main.html')


def my_view(request):
    users = Book.objects.all()
    return render(request, 'spisok.html', {'users': users})


grade = Grade()


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GradeForm
from .models import Grade

@login_required
def grade_list(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            selected_grades = form.cleaned_data['product']
            Grade.objects.all().update(is_visible=False)  # Сбросить все
            selected_grades.update(is_visible=True)  # Обновить выбранные
            return redirect('grade_list')
    else:
        form = GradeForm()
    grades = Grade.objects.all()
    return render(request, 'grade-list.html', {'grades': grades, 'form': form})


class MyDetailView1(DetailView):
    model = Book
    template_name = 'detail.html'
    context_object_name = 'book'



@login_required
def grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            selected_grades = form.cleaned_data['product']
            Grade.objects.all().update(is_visible=False)  # Сбросить все
            selected_grades.update(is_visible=True)  # Обновить выбранные
            return redirect('grade_list')
    else:
        form = Grade()
    grades = Grade.objects.all()
    return render(request, 'grade.html', {'grades': grades, 'form': form})
def author(request):
     authors = Author.objects.all()
     return render(request, 'author.html', {'authors': authors})


def registr(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            users = form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/registr.html', {'form': form})
