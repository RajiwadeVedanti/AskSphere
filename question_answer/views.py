from django.shortcuts import render
from rest_framework.views import APIView
from .serializers.question import QuestionSerializer
from .serializers.answer import AddAnswerSerializer
from .repository.question import QuestionRepository
from .repository.answer import AnswerRepository


class QuestionView(APIView):
    def post(self, request):
        user_id = request.session["user_id"]
        request_data = QuestionSerializer(data=request.data)
        if not request_data.is_valid():
            error_key = list(request_data.errors.keys())[0]
            error_msg = request_data.errors[error_key][0]
            return render(request, 'question_answer.html', {'errors': error_msg})
                
        result = QuestionRepository().post_question(request, request_data.data, user_id)
        return result


class QuestionListView(APIView):
    def get(self, request):
        result = QuestionRepository().posted_questions_list(request)
        return result
 
class AddAnswerView(APIView):
    def post(self, request):
        user_id = request.session["user_id"]
        request_data = AddAnswerSerializer(data=request.data)
        if not request_data.is_valid():
            error_key = list(request_data.errors.keys())[0]
            error_msg = request_data.errors[error_key][0]
            return render(request, 'question_answer.html', {'errors': error_msg})
        
        result = AnswerRepository().add_answer(request, user_id)

        return result
    

class LikedAnswerView(APIView):
    def post(self, request, answer_id):
        user_id = request.session["user_id"]
        result = AnswerRepository().add_like_to_answer(request, answer_id, user_id)
        return result
