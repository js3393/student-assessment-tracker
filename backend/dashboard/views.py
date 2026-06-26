from django.http import HttpResponse
from django.shortcuts import redirect, render
from tracker.models import TeacherProfile, Classroom, Enrollment, School

def dashboard_view(request):

      
      #If you want to see request.user commands and attributes uncomment below and it will show in browser
      # for index, item in enumerate(dir(request.user)):
      # output = ""
      #     output += item + "\n"

      #     if (index + 1) % 10 == 0:
      #         output += "\n"

      # return HttpResponse(f"<pre>{output}</pre>")

      current_user = request.user
      group_names = [group.name for group in current_user.groups.all()]
      if current_user.is_authenticated:
            if "Admins" in group_names:
                  return redirect("/admin/")
            
            elif "Teachers" in group_names:
                   try:
                         teacher_profile = TeacherProfile.objects.get(
                              user_account=current_user
                        )
                         first_name = teacher_profile.user_account.first_name
                         last_name = teacher_profile.user_account.last_name
                         title = teacher_profile.title
                         start_date = teacher_profile.start_date
                         classrooms = Classroom.objects.filter(teachers=teacher_profile)
                         schools = School.objects.filter(classroom__in=classrooms).distinct()
                         enrollments = Enrollment.objects.filter(classroom__in=classrooms)
#                          output = f"""<pre>
# Teacher: {first_name} {last_name}
# Title: {title}
# Start Date: {start_date}

# Classroom Count: {classrooms.count()}
# School Count: {schools.count()}
# Enrollment Count: {enrollments.count()}

# Classrooms:
# """

#                          for classroom in classrooms:
#                               output += f"- {classroom.name} | School: {classroom.school.name}\n"

#                          output += "\nStudents:\n"

#                          for enrollment in enrollments:
#                               output += f"- {enrollment.student.first_name} {enrollment.student.last_name} | Classroom: {enrollment.classroom.name}\n"

#                               output += "</pre>"

                         return HttpResponse()
                  
          
                   except TeacherProfile.DoesNotExist:
                        return HttpResponse("Teacher user has no TeacherProfile assigned.")
                  
                            
            
    #if current_user.is_authenticated:
     #   if current_user.is_staff:
        #    return render(request, 'dashboard/')
