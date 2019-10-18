from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup_view(req):
    if req.method=="POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            # log the use in
            return redirect('account:login')
            # return HttpResponseRedirect(reversed('articles:Articles_List'))
        return render(req,'account/signup.html',{'form':form})
    else:
        form = UserCreationForm()
        return render(req,'account/signup.html',{'form':form})

def login_view(req):
    if req.method == "POST":
        # pass
        form=AuthenticationForm(data=req.POST)
        if form.is_valid():
            # login the user
            user=form.get_user()
            login(req,user)
            if 'next' in req.POST:
                return redirect(req.POST.get('next'))
            return redirect('articles:Article_List')
    else:
        form = AuthenticationForm()

    return render(req,'account/login.html',{'form':form})

@login_required
def logout_view(req):
    if req.method=='GET':
        logout(req)
        return redirect('articles:Article_List')

