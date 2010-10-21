from django.conf.urls.defaults import *
from myproject.polls.models import Candidato

info_dict = {
    'queryset': Candidato.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^q=(?P<iden>.+)$', 'myproject.polls.views.plp_candidato_list'),
    (r'^(?P<object_id>\d+)/$', 'myproject.polls.views.plp_candidato_form'),
    (r'^(?P<object_id>\d+)/results/$', 'myproject.polls.views.plp_results'),
    (r'^(?P<candidato_id>\d+)/vote/$', 'myproject.polls.views.plp_vote'),
)
