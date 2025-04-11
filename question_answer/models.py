from django.db import models
from django.db.models import Model, AutoField, CharField, ForeignKey, DateTimeField, TextField
from auth_user.models import CustomUser

class Questions(Model):
    id = AutoField(null=False, primary_key=True)
    question = CharField(max_length=1000, null=False, db_index=True)
    posted_by = ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="questions_posted", null=False)
    created_on = DateTimeField(auto_now_add=True)

class Answers(Model):
    id = AutoField(null=False, primary_key=True)
    answer = TextField(null=False, db_index=True)
    posted_by = ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="answers_posted", null=False)
    question = ForeignKey(Questions, on_delete=models.CASCADE, related_name="answers", null=False)
    created_on = DateTimeField(auto_now_add=True)


class LikedAnswers(Model):
    id = AutoField(null=False, primary_key=True)
    liked_by = ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="answer_liked", null=False)
    answer = ForeignKey(Answers, on_delete=models.CASCADE, related_name="answer_liked", null=False)
    created_on = DateTimeField(auto_now_add=True)