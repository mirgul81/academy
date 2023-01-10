
from django.db import models


class Academy(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=50)
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




