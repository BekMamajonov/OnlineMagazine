from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Email yoki login",
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-custom',
            'placeholder': 'Loginni kiriting',
            'autocomplete': 'off'
        })
    )
    password = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-custom',
            'placeholder': '••••••••'
        })
    )

class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'bek'})
    )
    password = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-custom', 'placeholder': '••••'})
    )
    confirm_password = forms.CharField(
        label="Parolni tasdiqlash",
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-custom', 'placeholder': '••••'})
    )