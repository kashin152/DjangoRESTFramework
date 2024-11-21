from rest_framework.serializers import ModelSerializer, SerializerMethodField

from courses.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class LessonCountSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    @staticmethod
    def get_lesson_count(obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('id', "title", "description", "lessons", "lesson_count")
