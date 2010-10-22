from myproject.polls.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext, Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
#from django.views.decorators.csrf import csrf_protect
# import the logging library
import logging

# Get an instance of a logger

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

from django import forms
from captcha.fields import CaptchaField
from django.shortcuts import render_to_response

class CaptchaTestForm(forms.Form):
#    myfield = AnyOtherField()
    captcha = CaptchaField(error_messages= { "invalid": "Se pudrio"})

"""
# or, as a ModelForm:
class CaptchaTestModelForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = MyModel
"""

def s_captcha_simple(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically 
        # check the input
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render_to_response('polls/base.html',locals())

def umkt_quiero(request):
    if request.method == "POST":
       logging.debug("FORM_DATA: "+str(request.POST))
    return HttpResponseRedirect("ofrecen.html")
#   return HttpResponse("Hola, funciona FORM_DATA: "+str(request.POST))

def plp_candidato_list(request, iden):
	o= Candidato.objects.filter(identificadorcandidato__identificador__desc= iden)
	return render_to_response('polls/candidato_list.html', {'object_list': o, 'iden': iden})

def plp_candidato_list_r(request, rubro_id):
	o= Candidato.objects.filter(rubro__key=rubro_id)
	return render_to_response('polls/candidato_list.html', {'object_list': o, 'iden': "rubro "+ Rubro.objects.get(key=rubro_id).desc})


def plp_candidato_form(request, object_id):
    #XXX: generalizar, la unica diferencia con la vista generica es crear el captcha form
    try:
        p = Candidato.objects.get(pk=object_id)
    except Candidato.DoesNotExist:
        raise Http404

    form = CaptchaTestForm()
    return render_to_response('polls/candidato_form.html', {'object': p, 'form': form})

def plp_results(request, object_id):
    try:
        p = Candidato.objects.get(pk=object_id)
    except Candidato.DoesNotExist:
        raise Http404

    categorias= []
    vx= votoCntForCandidato(p)
    vmax= 1;
    for k in vx:
        vc= vx.get(k)
        if vmax < vc:
            vmax= vc

    for varDef in p.rubro.variablepararubro_set.all():
	opts= []
	for varOpt in varDef.variableDef.variableopt_set.all(): 
            vc= vx.get(varDef.variableDef.desc + "/" + varOpt.desc,0)
            opts.append({ 'desc': varOpt.desc, 'votos': vc , 'width': int(vc*10/vmax) , 'color': 'green'})

        categorias.append({ 'desc': varDef.variableDef.desc, 'opts': opts})

    return render_to_response('polls/candidato_results.html', {'object': p, 'categorias': categorias} )


def plp_vote(request, candidato_id):
    c = get_object_or_404(Candidato, pk=candidato_id)
    if request.POST:
        form = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically 
        # check the input
        if form.is_valid():
            human = True
            for vpr in c.rubro.variablepararubro_set.all():
               try:
                   if (vpr.variableDef.tipo=="O"):
                       val = vpr.variableDef.variableopt_set.get(pk=request.POST['v_'+str(vpr.id)])
                   else:
                       val = request.POST['v_'+str(vpr.id)]

               except (KeyError, ObjectDoesNotExist):
                   # Redisplay the poll voting form.
                   #XXX: mostrar cartelito
                   pass
               else:
                   #A: consegui la variable de la def (no de la web) y busque el valor en la def (no en la web), no preciso mas validaciones
                   logging.debug("XXX " + str(vpr.variableDef.desc) + " T="+ vpr.variableDef.tipo)
                   if (vpr.variableDef.tipo=="O"):
                       votarOptForCandidato(c,val)
                   else:
                       logging.debug("XXX VOTO R "+str(val))
               # Always return an HttpResponseRedirect after successfully dealing
               # with POST data. This prevents data from being posted twice if a
               # user hits the Back button.
            return HttpResponseRedirect(reverse('candidato_results', args=(c.id,)))
        else:
            return plp_candidato_form(request, candidato_id)

