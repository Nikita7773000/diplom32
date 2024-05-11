from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Book(models.Model):
    name = models.CharField('Название задач', max_length=50)
    author = models.CharField('Автор', max_length=50)
    title = models.TextField('Cодержание')
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField('Фамилия и имя', max_length=50)
    biography = models.TextField('задачи ')

    def __str__(self):
        return self.name


class Grade(models.Model):
    book = models.CharField('Название задачи№', max_length=50)
    grade = models.CharField('Задача', max_length=50)
    text = models.TextField('Описание')
    is_visible = models.BooleanField(default=False)



