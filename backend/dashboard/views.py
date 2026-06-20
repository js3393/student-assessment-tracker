from django.http import HttpResponse
from django.shortcuts import redirect, render
from tracker.models import TeacherProfile

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
                  teacher_profile = TeacherProfile.objects.get(
                        user_account=current_user
                        )
                  first_name = teacher_profile.user_account.first_name
                  last_name = teacher_profile.user_account.last_name
                  title = teacher_profile.title
                  program_location = teacher_profile.program_location
                  start_date = teacher_profile.start_date
                  return HttpResponse(
                        f"""
                        Teacher: {first_name} {last_name}
                        Title: {title}
                        Location: {program_location}
                        Start Date: {start_date}
                        """
                        )
          
                            
                  



    #if current_user.is_authenticated:
     #   if current_user.is_staff:
        #    return render(request, 'dashboard/')
