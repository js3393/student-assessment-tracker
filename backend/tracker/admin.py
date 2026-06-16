from django.contrib import admin

from .models import TeacherProfile, School, Classroom, Student, Enrollment, AttendanceRecord

admin.site.register(TeacherProfile)
admin.site.register(School)
admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(AttendanceRecord)