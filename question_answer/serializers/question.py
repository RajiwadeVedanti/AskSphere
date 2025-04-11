from rest_framework.serializers import Serializer, ModelSerializer, SerializerMethodField , CharField, IntegerField
from ..models import Questions
from ..serializers.answer import AnswerSerializer


class QuestionSerializer(Serializer):
    question = CharField(required=True)

    class Meta:
        model = Questions

class QuestionResponseSerializer(ModelSerializer):
    posted_by_user = SerializerMethodField()
    answers = SerializerMethodField()

    def get_posted_by_user(self, obj):
        return obj.posted_by.full_name
    
    def get_answers(self, obj):
        answer_data = obj.answers.all()
        return AnswerSerializer(answer_data, many=True).data

    class Meta:
        model = Questions
        fields = ["id", "question", "posted_by_user" ,"created_on", "answers"]
    