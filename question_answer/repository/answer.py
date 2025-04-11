
import logging
from django.shortcuts import redirect, render
from ..models import Questions, Answers, LikedAnswers
from auth_user.models import CustomUser


logger = logging.getLogger(__name__)

class AnswerRepository:
    def add_answer(self, request, user_id):
        try:

            request_data = request.data
            question = Questions.objects.get(id=request_data.get("question_id"))
            user = CustomUser.objects.get(id=user_id)

            answer = Answers.objects.create(
                question=question,
                answer=request_data.get("answer"),
                posted_by=user
            )
            answer.save()

            return redirect("/qa/get-question")
        except Questions.DoesNotExist:
            return render(request, 'question_answer.html', {'errors': "Question does not exists"})
        except CustomUser.DoesNotExist:
            return render(request, 'question_answer.html', {'errors': "User does not exists"})
        except Exception as e:
            logger.exception(f"add_answer exception: {str(e)}")
            return render(request, 'question_answer.html', {'errors': "Unexpected error occured!"})
    
    
    def add_like_to_answer(self, request, answer_id, user_id):
        try:
            answer = Answers.objects.get(id=answer_id)

            user = CustomUser.objects.get(id=user_id)


            ex_like_answer = LikedAnswers.objects.filter(
                answer=answer,
                liked_by=user
            )
            if ex_like_answer.count() == 0:
                like_answer = LikedAnswers.objects.create(
                    answer=answer,
                    liked_by=user
                )
                like_answer.save()

            return redirect("/qa/get-question")
        except Answers.DoesNotExist:
            return render(request, 'question_answer.html', {'errors': "Answer does not exists"})
        except CustomUser.DoesNotExist:
            return render(request, 'question_answer.html', {'errors': "User does not exists"})
        except Exception as e:
            logger.exception(f"add_like_to_answer exception: {str(e)}")
            return render(request, 'question_answer.html', {'errors': "Unexpected error occured!"})
