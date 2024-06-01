from django import forms


class SendEmailForm(forms.Form):
    email = forms.EmailField()


class LoginForm(forms.Form):
    email = forms.EmailField()
    token = forms.UUIDField()
