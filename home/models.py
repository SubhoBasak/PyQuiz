from django.db import models
from django.contrib.auth.models import User


class Score(models.Model):
    user = models.ForeignKey(verbose_name='User', to=User, on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name='Score', default=0)
    start_date_time = models.DateTimeField(verbose_name='Starting time', null=True)
    end_date_time = models.DateTimeField(verbose_name='Finishing time', auto_now_add=True)

    @property
    def full_name(self):
        return self.user.first_name+' '+self.user.last_name

    def __str__(self):
        return self.user.username


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    q1w1 = models.CharField(max_length=3)
    q1w2 = models.CharField(max_length=3)
    q1w3 = models.CharField(max_length=3)
    q1w4 = models.CharField(max_length=3)
    q1w5 = models.CharField(max_length=3)

    q2w1 = models.CharField(max_length=3)
    q2w2 = models.CharField(max_length=3)
    q2w3 = models.CharField(max_length=3)
    q2w4 = models.CharField(max_length=3)
    q2w5 = models.CharField(max_length=3)

    q3w1 = models.CharField(max_length=3)
    q3w2 = models.CharField(max_length=3)
    q3w3 = models.CharField(max_length=3)
    q3w4 = models.CharField(max_length=3)
    q3w5 = models.CharField(max_length=3)

    q4w1 = models.CharField(max_length=3)
    q4w2 = models.CharField(max_length=3)
    q4w3 = models.CharField(max_length=3)
    q4w4 = models.CharField(max_length=3)
    q4w5 = models.CharField(max_length=3)

    q5w1 = models.CharField(max_length=3)
    q5w2 = models.CharField(max_length=3)
    q5w3 = models.CharField(max_length=3)
    q5w4 = models.CharField(max_length=3)
    q5w5 = models.CharField(max_length=3)

    q6w1 = models.CharField(max_length=3)
    q6w2 = models.CharField(max_length=3)
    q6w3 = models.CharField(max_length=3)
    q6w4 = models.CharField(max_length=3)
    q6w5 = models.CharField(max_length=3)

    q7w1 = models.CharField(max_length=3)
    q7w2 = models.CharField(max_length=3)
    q7w3 = models.CharField(max_length=3)
    q7w4 = models.CharField(max_length=3)
    q7w5 = models.CharField(max_length=3)

    q8w1 = models.CharField(max_length=3)
    q8w2 = models.CharField(max_length=3)
    q8w3 = models.CharField(max_length=3)
    q8w4 = models.CharField(max_length=3)
    q8w5 = models.CharField(max_length=3)

    q9w1 = models.CharField(max_length=3)
    q9w2 = models.CharField(max_length=3)
    q9w3 = models.CharField(max_length=3)
    q9w4 = models.CharField(max_length=3)
    q9w5 = models.CharField(max_length=3)

    q10w1 = models.CharField(max_length=3)
    q10w2 = models.CharField(max_length=3)
    q10w3 = models.CharField(max_length=3)
    q10w4 = models.CharField(max_length=3)
    q10w5 = models.CharField(max_length=3)

    def get_answer(self):
        answer_set = []
        tmp = [self.q1w1, self.q1w2, self.q1w3, self.q1w4, self.q1w5]
        tmp.sort()
        answer_set.append(tmp)
        tmp = [self.q2w1, self.q2w2, self.q2w3, self.q2w4, self.q2w5]
        tmp.sort()
        answer_set.append(tmp)
        tmp = [self.q3w1, self.q3w2, self.q3w3, self.q3w4, self.q3w5]
        tmp.sort()
        answer_set.append(tmp)
        tmp = [self.q4w1, self.q4w2, self.q4w3, self.q4w4, self.q4w5]
        tmp.sort()
        answer_set.append(tmp)
        tmp = [self.q5w1, self.q5w2, self.q5w3, self.q5w4, self.q5w5]
        tmp.sort()
        answer_set.append(tmp)
        tmp = [self.q6w1, self.q6w2, self.q6w3, self.q6w4, self.q6w5]
        tmp.sort()
        answer_set.append(tmp)
        tmp = [self.q7w1, self.q7w2, self.q7w3, self.q7w4, self.q7w5]
        tmp.sort()
        answer_set.append(tmp)
        tmp = [self.q8w1, self.q8w2, self.q8w3, self.q8w4, self.q8w5]
        tmp.sort()
        answer_set.append(tmp)
        tmp = [self.q9w1, self.q9w2, self.q9w3, self.q9w4, self.q9w5]
        tmp.sort()
        answer_set.append(tmp)
        tmp = [self.q10w1, self.q10w2, self.q10w3, self.q10w4, self.q10w5]
        tmp.sort()
        answer_set.append(tmp)
        return answer_set