from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    course = models.ManyToManyField("Course", blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        verbose_name_plural = 'People'
        ordering = ('last_name', 'first_name' )


class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name}, {self.year}"

    class Meta:
        unique_together = ("name", "year")


class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.__str__()} --> {self.grade} --> {self.course.__str__()}"


