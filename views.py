from django.http import Http404, HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "singlepage/index.html")

    texts = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Praesent euismod auctor quam, id congue tellus malesuada vitae.",
    "Morbi imperdiet nunc ac quam hendrerit faucibus."]


    def section(request, num):
        if 1 <= num <= 3:
            return HttpResponse(texts[num - 1])
            else:
                raise Http404("No such section")

