from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from datetime import datetime
from .models import Activity, TimeLog

def index(request):
    """
    Shows a list of all activities and how long has been spent on each activity.
    """
    activities = Activity.objects.all()
    return render(request, 'index.html', {
        'activities': activities
    })

def new_activity(request):
    """
    Displays a form for creating a new Activity.
    On POST, create the Activity and redirect to its detail page.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            activity = Activity.objects.create(name=name)
            return redirect('activity_detail', activity_id=activity.id)
    return render(request, 'new_activity.html')

def activity_detail(request, activity_id):
    """
    Shows details about a specific activity: name, total time, and time logs.
    """
    activity = get_object_or_404(Activity, id=activity_id)
    time_logs = activity.timelog_set.all().order_by('-start_time')
    return render(request, 'activity_detail.html', {
        'activity': activity,
        'time_logs': time_logs
    })

def new_timelog(request, activity_id):
    """
    Displays a form for creating a new TimeLog for the specified Activity.
    On POST, parse the datetime and create a new TimeLog, then redirect.
    """
    activity = get_object_or_404(Activity, id=activity_id)
    if request.method == 'POST':
        start_time_str = request.POST.get('start_time')
        end_time_str = request.POST.get('end_time')
        if start_time_str and end_time_str:
            start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')
            end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M')
            TimeLog.objects.create(activity=activity, start_time=start_time, end_time=end_time)
            return redirect('activity_detail', activity_id=activity.id)
    return render(request, 'new_timelog.html', {
        'activity': activity
    })
