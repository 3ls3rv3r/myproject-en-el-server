from django.conf.urls.defaults import *
from myproject.polls.models import Candidato

info_dict = {
    'queryset': Candidato.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
    url(r'^(?P<object_id>\d+)/results/$', 'django.views.generic.list_detail.object_detail', 
dict(info_dict, template_name='polls/plp_results.html'), 'plp_results'),
    (r'^(?P<candidato_id>\d+)/vote/$', 'myproject.polls.views.plp_vote'),
)
