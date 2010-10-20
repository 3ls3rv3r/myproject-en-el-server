from django.conf.urls.defaults import *
from myproject.polls.models import Candidato

info_dict = {
    'queryset': Candidato.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
#GENERICO, no nos da captcha    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
    (r'^(?P<object_id>\d+)/$', 'myproject.polls.views.plp_detail'),
    (r'^(?P<object_id>\d+)/results/$', 'myproject.polls.views.plp_results'),
    (r'^(?P<candidato_id>\d+)/vote/$', 'myproject.polls.views.plp_vote'),
)
