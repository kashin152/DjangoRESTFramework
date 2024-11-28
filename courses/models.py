from django.db import models

from users.models import CustomsUser


class Course(models.Model):
    """Модель курса"""

    title = models.CharField(max_length=150, verbose_name="Название курса")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    preview = models.ImageField(upload_to="course/photo", null=True)
    owner = models.ForeignKey(
        CustomsUser,
        verbose_name="Владелец",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

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
    preview = models.ImageField(upload_to="course/photo", null=True)
    link_to_video = models.URLField(max_length=200)
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    owner = models.ForeignKey(
        CustomsUser,
        verbose_name="Владелец",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.title} - {self.description}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["title"]


class Subscription(models.Model):
    """Модель подписки"""

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomsUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "course")
