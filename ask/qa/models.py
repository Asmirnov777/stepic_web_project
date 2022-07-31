from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

class QuestionManager(models.Manager):
    def new(self):        
        return self.all().order_by('-id')  # [0:10]

    def popular(self):
        return self.all().order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='author', on_delete=models.DO_NOTHING, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', null=True, blank=True)
    objects = QuestionManager()

    def __unicode__(self):
        return self.title
#    def get_absolute_url(self):
#        return '/post/%d/' % self.pk
#    class Meta:
#        db_table = 'questions'
#        ordering = ['-creation_date']    


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)


#class Session(models.Model):
#    key = models.CharField(unique=True, max_length=255)
#    user = models.ForeignKey(User, blank=True, on_delete=models.DO_NOTHING)
#    expires = models.DateTimeField()
