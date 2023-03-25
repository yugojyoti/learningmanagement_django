from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,AnswerForm
# Create your views here.
def home(request):
    return render(request,"users/home.html")

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST) # save registed value in a dict
        #check wheater entered value are correct
        if form.is_valid():
            form.save() #save it in databases
            username=form.cleaned_data.get("username")
            message.success(request,f"Account Created for {username}!")
            return redirect("login")

    else:
        form=UserRegisterForm()

    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            message.sucess(request, f"Profile Sucessfully Updated!")
            return redirect("profile")

    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.profile)
        context={"u_form":u_form, "p_form":p_form}
        return render (request, "user/profile.html",context)


@login_required
def results(request):
    pass
