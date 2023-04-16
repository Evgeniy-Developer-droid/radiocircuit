
from django import forms
from forum_app.models import Topic, Message
from ckeditor.widgets import CKEditorWidget


class NewMessageForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(config_name='public'), required=True)
    class Meta:
        model = Message
        fields = ("body",)
	
    def __init__(self, *args, **kwargs):
        super(NewMessageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
