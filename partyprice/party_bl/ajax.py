from django.db import models
from django.utils import simplejson 
from dajaxice.core import dajaxice_functions 
from dajaxice.decorators import dajaxice_register

# Create your models here.

@dajaxice_register
def primer(request,message):
    return_message=u'Полученное сообщение: {0}'.format(message)
    return simplejson.dumps({'message':return_message})