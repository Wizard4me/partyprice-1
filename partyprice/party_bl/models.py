# coding=UTF-8

from django.db import models
from django.utils import simplejson 
from dajaxice.core import dajaxice_functions 

# Create your models here.

class User(models.Model):
    Login=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    

    
class Peoples(models.Model):
    Name=models.CharField(max_length=50)
    Group=models.CharField(max_length=50)
    User_link=models.ForeignKey(User)
    
    # delete object
    def Delete(self, params):
        p=Peoples.objects.get(pk=params['id'])
        p.delete()
        
    # do or edit object
    def Save(self, param):
        f=get(params['id'])
        if f=None:
            p=Peoples()
        else:
            p=Peoples.objects.get(id=Params['id'])
        p.Name=Params['Name']
        p.Group=Params['Group']
        p.User_link=Params['User_link']
        p.Save()
        return p.id 
    
    # return list 
    def List(self, params):
        return Peoples.objects.filter(User_link=Params['id']).values()
    
    
        
class Categorys(models.Model):
    Name=models.CharField(max_length=50)
    Specification=models.TextField()
    User_link=models.ForeignKey(User)
    
    # delete object
    def Delete(self, params):
        p=Categorys.objects.get(pk=params['id'])
        p.delete()
        
    # do or edit object
    def Save(self, param):
        f=get(params['id'])
        if f=None:
            p=Categorys()
        else:
            p=Categorys.objects.get(id=Params['id'])
        p.Name=Params['Name']
        p.Specification=Params['Specification']
        p.User_link=Params['User_link']
        p.Save()
        return p.id 
    
    # return list 
    def List(self, params):
        return Categorys.objects.filter(User_link=Params['id']).values()
    
    
class Action(models.Model):
    Name=models.CharField(max_length=50)
    Date=models.DateField(auto_now=False, auto_now_add=True)
    User_link=models.ForeignKey(User)
    
    # delete object
    def Delete(self, params):
        p=Action.objects.get(pk=params['id'])
        p.delete()
    
    # do or edit object
    def Save(self, param):
        f=get(params['id'])
        if f=None:
            p=Action()
        else:
            p=Action.objects.get(id=Params['id'])
        p.Name=Params['Name']
        p.Date=Params['Date']
        p.User_link=Params['User_link']
        p.Save()
        return p.id
    
    # return list 
    def List(self, params):
        return Action.objects.filter(User_link=Params['id']).values()
    
class Categorys_for_people(models.Model):
    People_id=models.ForeignKey(Peoples)
    Category_id=models.ForeignKey(Categorys)
    
    #Save people
    def Save(self, Params):
        f=get(Params['id'])
        if f=None:
            p=Categorys_for_people()
        else:
            p=Categorys_for_people.objects.get(id=Params['id'])
        p.People_id=Params['People_id']
        p.Category_id=Params['Category_id']
        p.Save()
        return p.id
    
    #Delete people
    def Delete(self, Params):
        p=Categorys_for_people.objects.get(id=Params['id'])
        p.delete()
        
    
class Setting_categorys(models.Model):
    Quotient=models.FloatField()
    Category_1_id=models.ForeignKey(Categorys)
    Category_2_id=models.ForeignKey(Categorys)
    
    #save settings
    def Save(self, Params):
        f=get(Params['id'])
        if f=None
            p=Setting_categorys()
        else:
            p=Setting_categorys.object.get(id=Params['id'])
        p.Category_1_id=Params['Category_1_id']
        p.Category_2_id=Params['Category_2_id']
        p.Quotient=Params['Quotient']
        p.Save()
        return p.id
    
    #delete settings
    def Delete(self, Params):
        p=Setting_categorys.object.get(id=Params['id'])
        p.delete()
        

class Buys(models.Model):
    Name=models.CharField(max_length=50)
    Price=models.FloatField()
    Date=models.DateField(auto_now=False, auto_now_add=True)
    Category=models.ForeignKey(Categorys) 
    Action=models.ForeignKey(Action)
    
    #Save Buys
    def Save(selfself, Params):
        f=get(Params['id'])
        if f=None
            p=Buys()
        else 
            p=Buys.object.get(id=Params['id'])
        p.Name=Params['Name']
        p.Price=Params['Price']
        p.Date=Params['Date']
        p.Category=Params['Category']
        p.Action=Params['Action']
        p.Save()
        return p.id
    
    #Delete Buys
    def Delete(self, Params):
        p=Buys.object.get(id=Params['id'])
        p.delete()
        
    
class Partys(models.Model):
    Contribution=models.FloatField()
    Action_id=models.ForeignKey(Action)
    People_id=models.ForeignKey(People)
    
    #Save Party
    def Save(self, Params):
        f=get(Params['id'])
        if f=None
            p=Partys()
        else 
            p=Partys.object.get(id=Params['id'])
        p.Action_id=Params['Action_id']
        p.People_id=Params['People_id']
        p.Contribution=Params['Contribution']
        p.Save()
        return p.id
    
    #Delete Party
    def Delete(self, Params):
        p=Partys.object.get(id=Params['id'])
        p.delete()
    
    

def primer(request,message):
    return_message=u'Полученное сообщение: {0}'.format(message)
    return simplejson.dumps({'message':return_message})