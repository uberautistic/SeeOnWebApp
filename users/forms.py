from django import forms

from users.models import User


class UpdateUserForm(forms.ModelForm):
    first_name= forms.CharField(max_length=255,
                                required=True,
                                widget=forms.TextInput(attrs={'class':'personal-input'}))
    last_name = forms.CharField(max_length=255,
                                 widget=forms.TextInput(attrs={'class': 'personal-input'}))
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'add_photo'}))


    class Meta:
        model=User
        fields = ['first_name',
                  'last_name',
                  'profile_picture']
