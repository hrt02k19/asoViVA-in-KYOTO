from django.shortcuts import render
from django.http import HttpResponse

from allauth.exceptions import ImmediateHttpResponse
from allauth.account import app_settings
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup

import random, string
from .models import Profile
from .forms import CustomSignupForm, ProfileForm

# Create your views here.
class MySignupView(SignupView):
    form_class = CustomSignupForm

    def get_user_id(self, num):
        # <num>文字のランダムな文字列を生成
        return ''.join(random.choices(string.ascii_letters + string.digits, k=num))

    def form_valid(self, form):
        self.user = form.save(self.request)
        self.user.user_id = self.get_user_id(10)
        self.user.save()
        try:
            return complete_signup(
                self.request,
                self.user,
                app_settings.EMAIL_VERIFICATION,
                self.get_success_url(),
            )
        except ImmediateHttpResponse as e:
            return e.response


def profile_edit(request):
    obj = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profile = ProfileForm(request.POST, instance=obj)
        profile.save()
    params = {
        'form': ProfileForm(instance=obj),
    }
    return render(request,'asovi_app/profile_edit.html',params)
