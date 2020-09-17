#from django.shortcuts import render
from django.http import HttpResponse

from .models import ALBUMS

def index(request):
    message="hello, world !!!"
    return HttpResponse(message)


def listing(request):
    albums = [f"<li>{album['name']}</>" for album in ALBUMS]
    message = """<ul>{}</>""".format("\n".join(albums))
    return HttpResponse(message)