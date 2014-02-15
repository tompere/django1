from django.http import HttpResponse
from iamaq.models import IamaQ, IamaPeople
from django.template import RequestContext, loader

css_tags = ['w0', 'w1', 'w2', 'h0', 'h1', 'h2']
# Create your views here.
def index(request):
    return index(request)

def index(request, q_num=10):
    n = int(q_num)
    # questions_list = IamaQ.objects.order_by('id')[:n]
    people = IamaPeople.objects.order_by('id')[:n]
    template = loader.get_template('iamaq/index.html')
    context = RequestContext(request, {
        'people': people,
        'css_tags':css_tags
    })
    return HttpResponse(template.render(context))

def questionDetails(request, q_id):
    question_data = IamaQ.objects.get(id=q_id)
    template = loader.get_template('iamaq/questionData.html')
    context = RequestContext(request, {
        'question_data': question_data,
    })
    return HttpResponse(template.render(context))