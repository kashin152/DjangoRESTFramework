from rest_framework.serializers import ModelSerializer, SerializerMethodField

from courses.models import Course, Lesson, Subscription
from courses.validators import LinkToVideoValidator


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    def get_is_subscribed(self, obj):
        user = self.context["request"].user
        return Subscription.objects.filter(user=user, course=obj).exists()


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["title", "description", "preview", "link_to_video", "course", "owner"]
        extra_kwargs = {"link_to_video": {"required": False}}
        validators = [LinkToVideoValidator(field="link_to_video")]


class CourseCountSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    @staticmethod
    def get_lesson_count(obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ("id", "title", "description", "lessons", "lesson_count")
