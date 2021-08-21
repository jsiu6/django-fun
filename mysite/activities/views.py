from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Activity


def index(request):
    latest_activity_list = Activity.objects.order_by('-start_date')[:5]
    template = loader.get_template('activities/index.html')
    context = {
        'latest_activity_list': latest_activity_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, activity_id):
    try:
        activity = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist:
        raise Http404("Activity does not exist")
    return render(request, 'activities/detail.html', {'activity': activity})
def results(request, activity_id):
    response = "You're looking at the results of actvity %s."
    return HttpResponse(response % activity_id)
