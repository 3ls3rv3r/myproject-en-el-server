from myproject.polls.models import *
from django.template import RequestContext, Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
#from django.views.decorators.csrf import csrf_protect


#def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    t = loader.get_template('polls/index.html')
#    c = Context({
#        'latest_poll_list': latest_poll_list,
#    })
#    return HttpResponse(t.render(c))

#def detail(request, poll_id):
#    try:
#        p = Poll.objects.get(pk=poll_id)
#    except Poll.DoesNotExist:
#        raise Http404
#    return render_to_response('polls/detail.html', {'poll': p})


#def results(request, poll_id):
#    p = get_object_or_404(Poll, pk=poll_id)
#    return render_to_response('polls/results.html', {'poll': p})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))

def plp_vote(request, candidato_id):
    c = get_object_or_404(Candidato, pk=candidato_id)
    for vpr in c.rubro.variablepararubro_set.all():
        try:
            val = vpr.variableDef.variableopt_set.get(pk=request.POST['v_'+str(vpr.id)])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the poll voting form.
            #XXX: mostrar cartelito
            pass
        else:
            c.voto_set.create(variableOpt= val)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('plp_results', args=(c.id,)))


