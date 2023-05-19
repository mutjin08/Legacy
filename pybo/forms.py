from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'location', 'audio', 'image', 'output','npz']
        labels = {
            'subject': '제목',
            'content': '내용',
            'location': '장소',
            'audio': '오디오 파일',
            'image': '이미지 파일',
            'output': '3D 모델',
            'npz': 'npz 파일',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
