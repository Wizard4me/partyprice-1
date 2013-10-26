# coding=UTF-8
from django.utils import simplejson 
import models
from dajaxice.decorators import dajaxice_register

# Create your models here.

@dajaxice_register(method='GET')
@dajaxice_register(method='POST', name='other_post')
def hello(request):
    return simplejson.dumps({'message': 'yo ho ho, motherfucers'})

@dajaxice_register(method='GET')
@dajaxice_register(method='POST', name='other_post')
def PeopleList(request, people_id ):
    params = { 'id': int( people_id ) }
    res = models.Peoples().List( params )
    #return_message=u'Полученное сообщение: {0}'.format(message)
    return simplejson.dumps( str( res ) )