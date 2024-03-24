from django.shortcuts import render,redirect
from .models import ContactModule, CoursesModule, ScheduleModule, TeamDeatilsModule, TestimonialModule

# Create your views here.
def index(request):
    coursesData = CoursesModule.objects.all()
    scheduleData = ScheduleModule.objects.all()
    teamData = TeamDeatilsModule.objects.all()
    testimonialData = TestimonialModule.objects.all()
    context = {'courses': coursesData, 'events': scheduleData, 'team': teamData, 'testimonials': testimonialData}
    return render(request,'index.html', context)

def contact(request):
    if request.method == 'POST':
        data = ContactModule.objects.create(name = request.POST['name'],email = request.POST['email'],message = request.POST['message'])
        data.save()
        return redirect('/')
    else:
        return render(request,'index.html')