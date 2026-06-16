
from django.conf import settings

from django.db import models


# Create your models here.
class TeacherProfile(models.Model):
    user_account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    program_location = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    # Add any additional fields as needed

    def __str__(self):
        return f"{self.user_account.first_name} {self.user_account.last_name}"

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    # Add any additional fields as needed

    def __str__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(TeacherProfile, blank=True)
    # Add any additional fields as needed

    def __str__(self):
        return self.name

class Student(models.Model):
    class GradeLevel(models.TextChoices):
        KINDERGARTEN = "K", "Kindergarten"
        GRADE_1 = "1", "1st Grade"
        GRADE_2 = "2", "2nd Grade"
        GRADE_3 = "3", "3rd Grade"
        GRADE_4 = "4", "4th Grade"
        GRADE_5 = "5", "5th Grade"
        GRADE_6 = "6", "6th Grade"
        GRADE_7 = "7", "7th Grade"
        GRADE_8 = "8", "8th Grade"
        GRADE_9 = "9", "9th Grade"
        GRADE_10 = "10", "10th Grade"
        GRADE_11 = "11", "11th Grade"
        GRADE_12 = "12", "12th Grade"
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=2, choices=GradeLevel.choices)
    age = models.PositiveIntegerField()    
    # Add any additional fields as needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Enrollment(models.Model):
    class Semester(models.TextChoices):
        FALL = "fall", "Fall"
        SPRING = "spring", "Spring"
        SUMMER = "summer", "Summer"

    class StudentStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        COMPLETED = "completed", "Completed"

    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    classroom = models.ForeignKey("Classroom", on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    semester = models.CharField(max_length=10, choices=Semester.choices)
    year = models.PositiveIntegerField()
    student_status = models.CharField(max_length=20, choices=StudentStatus.choices)
    # Add any additional fields as needed

    def __str__(self):
        return f"{self.student} - {self.classroom}"

class AttendanceRecord(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField()
    # Add any additional fields as needed

    def __str__(self):
        return f"{self.enrollment} - {self.date} - {'Present' if self.present else 'Absent'}"
