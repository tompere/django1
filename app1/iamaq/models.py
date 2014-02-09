from django.db import models

# Create your models here.
class IamaQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    questionAuthor = models.CharField(max_length=200)
    answerAuthor = models.CharField(max_length=200)
    created = models.DateTimeField('date published')
    iama_permalink = models.CharField(max_length=500)
    def __str__(self):  # Python 3: def __str__(self):
        return self.question