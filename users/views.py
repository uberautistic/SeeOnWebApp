import os
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from movies.models import Movie
from users.forms import UpdateUserForm
from users.models import User, Watchlist, Recomendations


def Signup(request):
    response_data = {}
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        first_name = str(request.POST['name'])
        email = request.POST['email']
        password = request.POST['new-password']

        forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root', 'email',
                           'user', 'join', 'sql', 'static', 'python', 'delete']
        if first_name.lower() in forbidden_users:
            response_data['username_error'] = "The username entered is prohibibited,choose another one"
            response_data['register'] = "Error"
            return HttpResponse(JsonResponse(response_data))

        if '@' in first_name or '+' in first_name or '-' in first_name:
            response_data['username_error'] = "This is an Invalid user, Do not user these chars: @ , - , +"
            response_data['register'] = "Error"
            return HttpResponse(JsonResponse(response_data))

        if get_user_model().objects.filter(email__iexact=email).exists():
            response_data['username_error'] = "User with this username already exists."
            response_data['register'] = "Error"
            return HttpResponse(JsonResponse(response_data))

        new_user = get_user_model().objects.create(first_name=first_name, email=email)
        new_user.set_password(password)
        new_user.save()
        log_user = authenticate(email=email, password=password)
        if log_user is not None:
            login(request, log_user)
            response_data['register'] = 'Success'
        return HttpResponse(JsonResponse(response_data))
    return HttpResponse(JsonResponse(response_data))


def Login(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        email = request.POST.get('current-email')
        password = request.POST.get('current-password')
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                response_data = {'login': "Success"}
            else:
                response_data = {'user': "not active"}
        else:
            response_data = {'user': "nouser"}
    else:
        response_data = {'login': "Failed"}
    return HttpResponse(JsonResponse(response_data))


@login_required
def Profile(request):
    if request.method == 'GET':
        user_form = UpdateUserForm(instance=request.user)
        watchlistids = Watchlist.objects.filter(user=request.user).values_list('kpid', flat=True)
        watchlist = Movie.objects.filter(kpid__in=watchlistids)
        if request.user.is_calibrated:
            recomendations_ids = Recomendations.objects.filter(user=request.user).order_by('?').values_list('kpid',
                                                                                                            flat=True)[
                                 :5]
            recomendations = Movie.objects.filter(kpid__in=recomendations_ids)
        else:
            recomendations = []
        context = {
            'user_form': user_form,
            'watchlist': watchlist,
            'recomendations':recomendations,
            'watchlistids': watchlistids
        }
        return render(request, 'users/personal_account.html', context=context)
    else:
        profile_picture_path = request.user.profile_picture.path
        profile_picture_url = request.user.profile_picture.url
        user_form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            if request.FILES and profile_picture_url != '/media/users_pfps/user_pfp_placeholder.jpeg':
                os.remove(profile_picture_path)
            user_form.save()
            return redirect(to='profile')
        else:
            print(user_form.errors)
            user_form = UpdateUserForm(instance=request.user)
        context = {'user_form': user_form}
        return render(request, 'users/personal_account.html', context)

@login_required
def logout_user(request):
    logout(request)
    return redirect(to='homepage')
