import datetime

from django.db import models
from django.utils import timezone

# Three-step guide to make model changes:
# 1. Change the models
# 2. Run python manage.py makemigrations, to create migrations for those chanes.
# 3. Run python manage.py migrate, to apply those changes to the database.

# There are separate commands to make and apply migrations is because we'll commit
# migrations to version control system and ship them with the app, thus they're
# also useable by others.

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

    def __repr__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __repr__(self):
        return self.choice_text
