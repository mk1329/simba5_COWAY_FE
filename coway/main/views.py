from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'main/main.html')

def convpage(request):
    return render(request, 'main/conv/conv.html')

def convinfopage(request):
    return render(request, 'main/conv/conv_info.html')

def convmappage(request):
    return render(request, 'main/conv/conv_map.html')

def easyroadpage(request):
    return render(request, 'main/road/easy_road.html')

def roadchoicepage(request):
    return render(request, 'main/road/road_choice.html')

def shortroadpage(request):
    return render(request, 'main/road/short_road.html')