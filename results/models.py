from django.db import models
from quizes.models import Quiz
# Create your models here.
from django.contrib.auth.models import User

class Result(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.FloatField(help_text="score result")
    
    def __str__(self) -> str:
        return str(self.pk)