from django.urls import path
from .views import QuestionView, QuestionListView, AddAnswerView, LikedAnswerView


urlpatterns = [   
    path("post-question", QuestionView.as_view(), name="post_question"),
    path("get-question", QuestionListView.as_view(), name="get_questions"),
    path("add-answer", AddAnswerView.as_view(), name="add_answer"),
    path("add-like/<int:answer_id>", LikedAnswerView.as_view(), name="add_like_to_answer"),
]

