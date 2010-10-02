from django.db import models
from datetime import datetime

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

    was_published_today.short_description = 'Published today?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice

#S: Ponele los puntos
#S: definiciones
class VariableDef(models.Model):
    """ej. cuanto tardo en llegar"""
    desc = models.CharField(max_length=100)
    def __unicode__(self):
        return self.desc

class VariableOpt(models.Model):
    """ej. tardo en llegar=20min"""
    variableDef= models.ForeignKey(VariableDef)
    desc= models.CharField(max_length=20)
    def __unicode__(self):
        return self.desc

class Rubro(models.Model):
    """ej. Plomero"""
    desc = models.CharField(max_length=100)
    def __unicode__(self):
        return self.desc

class VariableParaRubro(models.Model):
    """ej. para Plomero 'cuanto tardo en llegar'"""
    rubro= models.ForeignKey(Rubro)
    variableDef= models.ForeignKey(VariableDef)

#S: instancias
class Candidato(models.Model):
    """ej. Juan Plomero"""
    desc = models.CharField(max_length=100)
    rubro= models.ForeignKey(Rubro)
    #XXX: telefono, mail, otras formas de IDENTIFICARLO
    def __unicode__(self):
        return self.desc

class Voto(models.Model):
    """ej. Juan Plomero tardo 20 min en llegar"""
    candidato= models.ForeignKey(Candidato)
    variableOpt= models.ForeignKey(VariableOpt)
    def __unicode__(self):
        return self.variableOpt.desc
