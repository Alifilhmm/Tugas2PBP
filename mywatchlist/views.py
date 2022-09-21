from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers


# TODO: Create your views here.
def show_mywatchlist(request):
    item_mywatchlist = MyWatchList.objects.all()
    context = {
        'item_mywatchlist': item_mywatchlist,
        'nama' : 'Alif',
    }
    return render(request, 'mywatchlist.html', context)


def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data = MyWatchList.objects.all()
    context = {
        'item_mywatchlist': data,
        'nama' : 'Alif',
    }
    return render(request, 'mywatchlist.html', context)
