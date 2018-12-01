from django.shortcuts import render
#sfrom django.http import HttpRequest

# Create your views here.
def index(request):
          content_dict={'text':'Hello World','numb': 100}
          return render(request,'basic_app/index.html',content_dict)

def others(request):
          return render(request,"basic_app/other.html")

def relative(request):
          return render(request,"basic_app/relative_url_templates.html")