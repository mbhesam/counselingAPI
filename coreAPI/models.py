from django.db import models


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='نام سوال')
    prefix_question = models.TextField(default=None, blank=True, verbose_name='پیش متن سوال')
    original_question = models.TextField(default=None, verbose_name='متن اصلی سوال')
    start = models.BooleanField(default=False, blank=True, verbose_name='آیا این اولین سوال ربات است؟')
    end = models.BooleanField(default=False, blank=True, verbose_name='آیا این پاسخ نهایی ربات است؟')

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'

    def __str__(self):
        return self.name

class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    original_answer = models.CharField(max_length=255, verbose_name='جواب')
    self_question = models.ForeignKey(to=Questions, related_name="self_answers", on_delete=models.CASCADE,
                                      verbose_name='سوال مربوط به این جواب')
    next_question = models.ForeignKey(to=Questions, related_name="last_answers", on_delete=models.CASCADE,
                                      verbose_name='سوال بعدی این جواب')

    class Meta:
        verbose_name = 'جواب'
        verbose_name_plural = 'جواب ها'

    def __str__(self):
        return f"{self.self_question} = {self.original_answer}"
