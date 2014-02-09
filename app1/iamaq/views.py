from django.shortcuts import render
from django.http import HttpResponse
from iamaq.models import IamaQ
from django.template import RequestContext, loader

# Create your views here.
def index(request):
    return index(request)

def index(request, q_num=10):
    n = int(q_num)
    questions_list = IamaQ.objects.order_by('id')[:n]
    template = loader.get_template('iamaq/index.html')
    context = RequestContext(request, {
        'questions_list': questions_list,
    })
    return HttpResponse(template.render(context))

def questionDetails(request, q_id):
    question_data = IamaQ.objects.get(id=q_id)
    template = loader.get_template('iamaq/questionData.html')
    context = RequestContext(request, {
        'question_data': question_data,
    })
    return HttpResponse(template.render(context))