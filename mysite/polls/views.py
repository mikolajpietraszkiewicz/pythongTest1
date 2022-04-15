from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


from django.template import loader




def index(request):

    template = loader.get_template('polls/index.html')
    context = {
       
    }
    return HttpResponse(template.render(context, request))