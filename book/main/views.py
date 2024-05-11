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


@login_required
def grade_list(request):
    grade = Grade.objects.all()
    if request.method == 'POST':
        form = GradeForm(request.POST)  # Загрузка данных в форму
        if form.is_valid():
            products = form.cleaned_data['product']
            for product in products:
                product.is_visible = True
                product.save()
            return redirect('grade_list')  # Перенаправление для предотвращения повторной отправки формы
    return render(request, 'grade-list.html', {'grade': grade})


class MyDetailView1(DetailView):
    model = Book
    template_name = 'detail.html'
    context_object_name = 'book'


@login_required
def grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-book')
    else:
        form = GradeForm()
    return render(request, 'grade.html', {'form': form})

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
