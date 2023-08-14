from django import forms
from accounts.models import ChatUser

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=50, required=True)
    password1 = forms.CharField(label='Password', max_length=256, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', max_length=256, required=True, widget=forms.PasswordInput)

    class Meta:
        model = ChatUser
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            acc = ChatUser.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username {username} is already in use!")
    
    def clean(self):
        password1 = self.cleaned_data['password1']
        print(self.cleaned_data)
        password2 = self.cleaned_data['password2']
        print(password1, password2)
        if password1 == password2:
            return self.cleaned_data
        else:
            raise forms.ValidationError('Passwords do not match!')
    

    def save(self):
        print(self.cleaned_data)
        user = ChatUser.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1']
        )

        return user

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50, required=True)
    password = forms.CharField(label='Password', max_length=256, required=True, widget=forms.PasswordInput)

    
    fields = ['username', 'password']
