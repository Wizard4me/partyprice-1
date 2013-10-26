# coding=UTF-8

from django.db import models
from django.utils import simplejson 
from dajaxice.core import dajaxice_functions 

# Create your models here.


def primer(request,message):
    return simplejson.dumps({'message':'Hello from Python!'})