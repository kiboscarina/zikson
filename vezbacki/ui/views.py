import json
from django.http.response import Http404, HttpResponse
from django.shortcuts import render 
from django.template.context_processors import request
from data.models import News, TrainingLocation
from data.models import Trainer



def training(request):
    return render( request,template_name= 'training.html') 

def primer(request):
    return render(request, template_name='primer.html')

def get_traning_locations(request):
    print(request.POST)
    lat = float(request.POST['lat'])
    lng = float(request.POST['lng'])
    x = 5
    training_found = TrainingLocation.objects.filter(
        lat__gt=lat - x,
        lat__lt=lat + x,
        lng__gt=lng - x,
        lng__lt=lng + x,
    )
    relevant_data = training_found.values('lng', 'lat')
    relevant_data = list(relevant_data)
    for item in relevant_data:
        item['lng'] = float(item['lng'])
        item['lat'] = float(item['lat'])
    
    return HttpResponse(json.JSONEncoder().encode(relevant_data))

def index(request):
    news = News.objects.all().order_by('-id')[:4]
    built_context = {
        'news':news
    }
    return render(request , template_name= 'index.html', context=built_context)
    
    
def log(request):
    if request.user.is_authenticated():
        return render(request , template_name= 'ui/index.html')
       
    
def treneri(request):
    trainer = Trainer.objects.all() 
    built_context = {
        'svi':trainer
    }
    if request.user.is_authenticated():
        return render(request , template_name= 'page.html' , context=built_context)    
    else:
        raise Http404('log in ')
     
    
def trainer(request, trainer_id):
    trainer = Trainer.objects.filter(pk=trainer_id).first()
    if trainer:
        built_context = { 'trainer': trainer }
        return render(request , template_name= 'trainer.html' , context=built_context)    
    else:
        raise Http404('nema trenera ')
    
    
def wholenews(request , news_id):   
    news = News.objects.filter(pk=news_id).first()
    if news:
        built_context = { 'news': news }
        return render(request , template_name= 'wholenews.html' , context=built_context)    
    else:
        raise Http404("OOPS")
    
    
   

    