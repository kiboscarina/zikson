from django.conf.urls import url, include
from ui import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', views.index, name='index'),
    url(r'^trainer/(?P<trainer_id>[0-9]+)$', views.trainer, name='trainer'),
    url(r'^wholenews/(?P<news_id>[0-9]+)$', views.wholenews, name='wholenews'),
    url(r'^training',views.training, name='training'),
    url(r'^primer',views.primer, name='primer'),
    url(r'^get_traning_locations',views.get_traning_locations, name='get_traning_locations'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)