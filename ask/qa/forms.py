from django import forms
from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=80)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, **kwargs):
        #self._user = user
        super(AskForm, self).__init__(**kwargs)

    def clean(self):
        return

    def save(self):
        self.cleaned_data['author'] = None
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    #question = forms.IntegerField()

    def __init__(self, question_id=None, **kwargs):
        #self._user = user
        self._question_id = question_id
        super(AnswerForm, self).__init__(**kwargs)

    def clean(self):
        return

    def save(self):
        self.cleaned_data['author'] = None
        self.cleaned_data['question'] = Question.objects.filter(id=self._question_id)[0]
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

#class WrongAnswerForm:
#    text = forms.CharField(widget=forms.Textarea)
#    def __init__(self, **kwargs):
#        super(WrongAnswerForm, self).__init__(**kwargs)
