from django.contrib import admin

from data.models import News
from data.models import Trainer, TrainingLocation


class TrainerDetails(admin.ModelAdmin):
    list_display = ('first_name' , 'last_name')
    search_fields = ('about', )    
admin.site.register(Trainer)



class NewsAdmin(admin.ModelAdmin):
    list_display = ('hedline',)
    search_fields = ('hedline','text')

admin.site.register(News, NewsAdmin)
    
    
admin.site.register(TrainingLocation)