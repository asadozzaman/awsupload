from django.shortcuts import render

# Create your views here.


from django.shortcuts import render


def hello(request, name):
    return render(request, "hello.html", {"name": name})

    # return HttpResponse("<b>Hello " + name +"</b>")
