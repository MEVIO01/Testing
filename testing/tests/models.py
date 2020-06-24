from django.db import models
from accounts.models import Account


class Test(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=200)
    tests = models.ManyToManyField(Test)

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=300)
    is_right = models.BooleanField()
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title


class Result(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    test = models.OneToOneField(Test, on_delete=models.CASCADE)
    result = models.FloatField()

    def __str__(self):
        return str(self.result)
