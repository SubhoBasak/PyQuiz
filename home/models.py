from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Exam(models.Model):
    title = models.CharField(max_length=200, default='')
    start = models.DateTimeField(verbose_name='Exam starting time')
    end = models.DateTimeField(verbose_name='Exam ending time')
    questions = models.IntegerField(verbose_name='Number of questions', default=1)

    def is_active(self):
        now = timezone.now()
        if self.start <= now and self.end > now:
            return True
        return False


class Score(models.Model):
    user = models.ForeignKey(verbose_name='User', to=User, on_delete=models.CASCADE, null=True)
    exam = models.ForeignKey(verbose_name='Exam', to=Exam, on_delete=models.CASCADE, null=True)
    score = models.IntegerField(verbose_name='Score', default=0)
    start = models.DateTimeField(verbose_name='Starting time', auto_now_add=True)
    end = models.DateTimeField(verbose_name='Ending time', auto_now_add=True)

    @property
    def full_name(self):
        return self.user.first_name+' '+self.user.last_name

    @property
    def exam_name(self):
        return self.exam.title

    @property
    def exam_score(self):
        return str(self.score)+'/'+str(self.exam.questions)

    @property
    def email(self):
        return self.user.email

    @property
    def full_marks(self):
        return self.exam.questions

    def __str__(self):
        return self.user.username


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=False)
    image = models.ImageField(verbose_name='Image', upload_to='Question image', null=True, blank=True)
    question = models.TextField(null=False, blank=False)
    optionA = models.CharField(verbose_name='Option A', max_length=200, null=False, blank=False)
    optionB = models.CharField(verbose_name='Option B', max_length=200, null=False, blank=False)
    optionC = models.CharField(verbose_name='Option C', max_length=200, null=False, blank=False)
    optionD = models.CharField(verbose_name='Option D', max_length=200, null=False, blank=False)
    answer = models.CharField(verbose_name='Answer',
                              choices=[('A', 'Option A'), ('B', 'Option B'),
                                       ('C', 'Option C'), ('D', 'Option D')],
                              max_length=1)

    def __str__(self):
        return self.question[:10]


class QuestionSet(models.Model):
    score = models.ForeignKey(Score, on_delete=models.CASCADE, null=True, blank=False)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    confidence = models.FloatField(verbose_name='Confidence', default=0.0)
    answered = models.CharField(verbose_name='Answered', default='', max_length=1)

    @property
    def question_text(self):
        return self.question.question

    @property
    def student_answer(self):
        if self.answered == 'A':
            return self.question.optionA
        elif self.answered == 'B':
            return self.question.optionB
        elif self.answered == 'C':
            return self.question.optionC
        elif self.answered == 'D':
            return self.question.optionD

    @property
    def actual_answer(self):
        if self.question.answer == 'A':
            return self.question.optionA
        elif self.question.answer == 'B':
            return self.question.optionB
        elif self.question.answer == 'C':
            return self.question.optionC
        elif self.question.answer == 'D':
            return self.question.optionD