import logging
from django.shortcuts import render, redirect
from ..models import Questions
from auth_user.models import CustomUser
from ..serializers.question import QuestionResponseSerializer

logger = logging.getLogger(__name__)

class QuestionRepository:
    def post_question(self, request, request_data, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            question = Questions.objects.create(
                question=request_data.get("question"),
                posted_by=user
            )
            question.save()
            return redirect("/qa/get-question")
        except CustomUser.DoesNotExist:
            return render(request, 'question_answer.html', {'errors': "User does not exists"})
        except Exception as e:
            logger.exception(f"post_question exception: {str(e)}")
            return render(request, 'question_answer.html', {'errors': "Unexpected error occured!"})
        
    def posted_questions_list(self, request):
        try:
            questions = Questions.objects.all().order_by("-created_on")
            data = QuestionResponseSerializer(questions, many=True).data
            return render(request, 'question_answer.html', {'question_data':data})
        except Exception as e:
            logger.exception(f"posted_questions_list exception: {str(e)}")
            return render(request, 'question_answer.html', {'errors': "Unexpected error occured!"})
        