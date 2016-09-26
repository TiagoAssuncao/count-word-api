from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from counter.serializers import CounterSerializer
from counter.models import Counter

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def counter_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        counters = Counter.objects.all()
        serializer = CounterSerializer(counters, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def get_counter(request):
    if request.method == 'POST':
        form = request.POST
        web_page = form.get('web_page')
        word = form.get('word')

        counter = Counter.objects.create(web_page=web_page, word=word)
        counter.save()

        content_page = counter.get_web_page()
        counter.count_words(content_page)

        serializer = CounterSerializer(counter)
        return JSONResponse(serializer.data)

    else:
        return JSONResponse(serializer.errors, status=400)
