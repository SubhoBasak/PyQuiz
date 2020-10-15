from django.contrib import admin
from .models import Score, Question, Exam, QuestionSet


class QuestionSetInline(admin.StackedInline):
    model = QuestionSet
    fields = ['question_text', 'student_answer', 'confidence', 'actual_answer']
    readonly_fields = ['question_text', 'student_answer', 'confidence', 'actual_answer']
    extra = 0


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'exam_name', 'exam_score', 'start', 'end']
    fields = ['full_name', 'email', 'exam_name', 'full_marks', 'score', 'start', 'end']
    readonly_fields = ['full_name', 'email', 'exam_name', 'full_marks', 'start', 'end']

    ordering = ['exam', 'user']
    inlines = [QuestionSetInline]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class ExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'start', 'end']
    inlines = [QuestionInline,]


admin.site.register(Score, ScoreAdmin)
admin.site.register(Exam, ExamAdmin)