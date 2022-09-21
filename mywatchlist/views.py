from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers


# TODO: Create your views here.
def show_mywatchlist(request):
    item_mywatchlist = MyWatchList.objects.all()
    notYetWatched = 0
    watched = 0
    message = ""
    for movie in item_mywatchlist:
        if (movie.watched):
            watched += 1
        else :
            notYetWatched += 1
    print(watched)

    if (notYetWatched <= watched):
        message = "Selamat, kamu sudah banyak menonton!"
    else :
        message = "Wah, kamu masih sedikit menonton!"
    context = {
        'item_mywatchlist': item_mywatchlist,
        'nama' : 'Alif',
        'message' : message,
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
