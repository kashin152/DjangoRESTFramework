from django.db import models


class Course(models.Model):
    """Модель курса"""

    title = models.CharField(max_length=150, verbose_name="Название курса")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    preview = models.ImageField(upload_to='course/photo', null=True)

    def __str__(self):
        return f"{self.title} - {self.description}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["title"]


class Lesson(models.Model):
    """Модель урока"""

    title = models.CharField(max_length=150, verbose_name="Название урока")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    preview = models.ImageField(upload_to='course/photo', null=True)
    link_to_video = models.URLField(max_length=200)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.description}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["title"]
