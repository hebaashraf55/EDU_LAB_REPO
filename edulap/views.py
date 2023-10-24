from django.shortcuts import get_object_or_404, redirect, render
from .models import Customer, Meeting, Courses,Category
from .forms import CustomerForm, CoursesForm, MeetingForm, CategoryForm
from django.views.generic import TemplateView , CreateView
# Create your views here.


def home(request):  
    meeting = Meeting.objects.all().order_by('-pk')[:5]
    courses = Courses.objects.all()
    form = CustomerForm()
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    context = {
               'meeting': meeting,
               'courses' : courses,
               'form': form,
               }
    return render(request, 'edulap/home.html', context)


def meeting(request):
    meeting = Meeting.objects.all()
    soon = Meeting.objects.order_by('-startDate')
    category = Meeting.objects.order_by('category')
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    context= {'meeting': meeting, 'soon':soon, 'category': category, 'form':form}
    return render(request,'edulap/meetings.html',context)


def meeting_detail(request, slug):
    meeting = get_object_or_404(Meeting, slug=slug)
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    context= {'meeting': meeting, 'form':form}
    return render(request,'edulap/meeting-details.html', context)



def courses(request):
    courses = Courses.objects.all()
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    context = {'courses': courses, 'form':form}
    return render(request, 'edulap/courses.html', context)

def course_detail(request, slug):
    course = get_object_or_404(Courses, slug=slug)
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    context = {'course': course,'form':form}
    return render(request, 'edulap/course-detail.html', context)