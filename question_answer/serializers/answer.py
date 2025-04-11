from rest_framework.serializers import Serializer, ModelSerializer, SerializerMethodField , CharField, IntegerField
from ..models import Answers

class AddAnswerSerializer(Serializer):
    question_id = IntegerField(required=True)
    answer = CharField(required=True)

    class Meta:
        model = Answers


class AnswerSerializer(ModelSerializer):
    ans_posted_by_user = SerializerMethodField()
    like_count = SerializerMethodField()

    def get_ans_posted_by_user(self, obj):
        return obj.posted_by.full_name
    
    def get_like_count(self, obj):
        return obj.answer_liked.count()

    class Meta:
        model = Answers
        fields = ["id", "answer", "ans_posted_by_user", "created_on", "like_count"]