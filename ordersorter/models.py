from django.db import models
import datetime
from django.utils import timezone
from django.utils.crypto import get_random_string
from jsonfield import JSONField
# from django.contrib.postgres.fields import ArrayField
# import JSONField
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User # new
from datetime import datetime


# class User(AbstractUser):
#     pass


def randomCode():
    #I left off O because it looks like a 0
    return get_random_string(length=6, allowed_chars='ABCDEFGHIJKLMNPQRSTUVWXYZ0123456789')


DEFAULT_USER_ID = 1
class Question(models.Model):
    question = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True)
    code = models.CharField(max_length=8, blank=True, default=randomCode)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID) # new
    pub_date = models.DateTimeField('date published', default=datetime.now, blank=True)
    # options = models.ManyToManyField(Option, blank=True, related_name="options")
    # results = models.ManyToManyField(Result, blank=True, related_name="results")

    def __str__(self):
        return f"{self.question}"

    # def serialize(self):
    #     return {
    #         "id":self.id,
    #         "question":self.question,
    #         "description":self.description,
    #         "code":self.code,
    #         "results":[result.name for result in self.results.all()],
    #         "options":[option.optionText for option in self.options.all()]
    #     }

# Create your models here.
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    optionText = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.optionText

    # def serialize(self):
    #     return {
    #         "id":self.id,
    #         "optionText":self.optionText,
    #         "question":self.question.question
    #     }


class Result(models.Model):
    name = models.CharField(max_length=64)
    order = JSONField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="results")
    pub_date = models.DateTimeField('date published', default=datetime.now, blank=True)
    # order = ArrayField(models.CharField(max_length=200))

    def __str__(self):
        return f"{self.name}" 

    # def serialize(self):
    #     return {
    #         "id":self.id,
    #         "order":self.order["items"],
    #         "question":self.question.question
    #     }

