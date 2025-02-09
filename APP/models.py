from django.db import models
import sqlite3


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data= models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text =  models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text



class Category(models.Model):
    category_name = models.CharField(max_length=200,default="Имя не присвоенно")
    category_picture= models.ImageField(upload_to='images/')
    def __str__(self):
          return self.category_name

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Катологи'
    

class People(models.Model):
   people_name = models.CharField(max_length=200)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   def __str__(self):
       return self.people_name
   class Meta:
        verbose_name = 'Известные Люди'
        verbose_name_plural = 'Люди'



