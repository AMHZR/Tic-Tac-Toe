# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404,HttpResponse

def index(request,template="base.django.html"):
    data={}
    return render_to_response(template,data,context_instance=RequestContext(request))

def game(request,template="index.django.html"):
    data={}
    return render_to_response(template,data,context_instance=RequestContext(request))