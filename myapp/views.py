from django.shortcuts import render

def about_me(request):
    return render(request, 'about_me.html')

def store(request):
    return render(request,'store.html')

def main(request):
    return render(request,'main.html')